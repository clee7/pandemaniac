import sys
import json
import numpy as np
import networkx as nx
from michelle_centrality import *
from operator import itemgetter
from dominating_set import *


def load_graph(filename):
    # Get the adjacency list
    with open(filename) as f:
        graph = json.load(f)
    return graph


def parse_file_path(file_path):
    parts = file_path.rsplit('/', 1)
    directory = ""
    filename = parts[0]
    if len(parts) >= 2:
        directory = parts[0] + "/"
        filename = parts[1]
    nums = filename.split('.')
    num_players = int(nums[0])
    num_seeds = int(nums[1])
    return (directory, filename, num_players, num_seeds)


def random_nodes_strategy(graph, num_seeds, num_rounds):
    # Get the list of nodes
    nodes = list(graph.keys())

    # Select random from nodes
    random_list = []
    np.random.shuffle(nodes)
    for i in range(num_seeds):
        random_list.append(nodes[i])
    return random_list * num_rounds


def highest_degree_strategy(graph, num_seeds, num_rounds):
    highest_degree = []
    i = 0
    for k in sorted(graph, key=lambda k: len(graph[k]), reverse=True):
        highest_degree.append(k)
        i += 1
        if i >= num_seeds:
            break
    return highest_degree * num_rounds


def betweenness_strategy(graph, num_seeds, num_rounds):
    betweenness_list = []
    new_nodes = nx.betweenness_centrality(graph, k=len(graph) / 10)
    for node in range(num_seeds):
        betweenness_list.append((node, new_nodes[str(node)]))
    betweenness_list.sort(key=operator.itemgetter(1), reverse=True)

    new_bet_list = [i[0] for i in betweenness_list]
    return new_bet_list * num_rounds


def eigenvector_strategy(graph, num_seeds, num_rounds):
    highest_eigenvectors = []
    node_values = nx.eigenvector_centrality(graph)

    top_eigenvalues = sorted(
        node_values.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    highest_eigenvectors = [i[0] for i in top_eigenvalues]
    return (highest_eigenvectors * num_rounds)


def closeness_strategy(graph, num_seeds, num_rounds):
    highest_closeness = []
    node_values = nx.closeness_centrality(graph)
    top_closeness = sorted(
        node_values.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    highest_closeness = [i[0] for i in top_closeness]
    return (highest_closeness * num_rounds)


def dominating_set_strategy(G, num_rounds, num_seeds):
    dominating_set = list(nx.dominating_set(G))

    # Obtaining seeds nodes from selecting the highest deg from the dominating
    seeds = []
    degrees = G.degree(dominating_set)
    print(degrees)
    i = 0
    for k in sorted(degrees, key=lambda k: k[1], reverse=True):
        seeds.append(k[0])
        i += 1
        if i >= num_seeds:
            break

    # if the size of dominating set is smaller than num of seed, randomly
    # select
    if len(seeds) < num_rounds:
        remaining_nodes = list(G.nodes()) - dominating_set
        np.random.shuffle(remaining_nodes)
        for i in range(num_rounds - len(seeds)):
            seeds.append(remaining_nodes[i])
    return seeds * num_rounds


def save_output(filename, strategies):

    file = open(filename, "w")
    for j in range(len(strategies)):
        file.writelines(str(strategies[j]) + '\n')
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python pandemaniac.py <path_to_json_file>")
        sys.exit(1)

    path = sys.argv[1]

    # Define global var
    num_rounds = 50

    # Parse the input path to find filename and number of players and seeds
    (directory, filename, num_players, num_seeds) = parse_file_path(path)

    # Find output file name
    output_filename = directory + filename.rsplit('.', 1)[0] + ".txt"

    # Get the adjacency list
    graph = load_graph(path)

    # Generate graph from nodes
    G = nx.from_dict_of_lists(graph)

    # Generate a list of random nodes as root nodes
    # strategy = random_nodes_strategy(graph, num_seeds, num_rounds)
    # strategy = highest_degree_strategy(graph, num_seeds, num_rounds)
    strategy = eigenvector_strategy(G, num_seeds, num_rounds)
    # strategy = dominating_set_strategy(G, num_seeds, num_rounds)

    # Save input file
    save_output(output_filename, strategy)
