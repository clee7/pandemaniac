import sys
import json
import math
import numpy as np
import networkx as nx
import operator
from collections import OrderedDict, Counter


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


def neighbor_highest_degree(graph, num_seeds, num_rounds):
    highest_degree = sorted(graph, key=lambda k: len(graph[k]),
                            reverse=True)[:num_seeds]
    neighbor = []
    for node in highest_degree:
        node_neighbors = {k: graph[k] for k in graph[node]}
        highest_neighbors = sorted(node_neighbors,
                                   key=lambda k: len(node_neighbors[k]),
                                   reverse=True)
        for i in highest_neighbors[:num_seeds]:
            neighbor.append(i)
    neighbor = sorted(neighbor, key=Counter(neighbor).get, reverse=True)
    neighbor = list(OrderedDict.fromkeys(neighbor))
    return neighbor[:num_seeds] * num_rounds


def betweenness_strategy(graph, num_seeds, num_rounds):
    betweenness_list = []
    new_nodes = nx.betweenness_centrality(graph, k=int(len(graph) / 10))
    top_betweenness = sorted(
        new_nodes.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    betweenness_list = [i[0] for i in top_betweenness]
    return (betweenness_list * num_rounds)


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


def katz_strategy(graph, num_seeds, num_rounds):
    highest_katz = []
    lam_max = max(nx.adjacency_spectrum(graph))
    node_values = nx.katz_centrality_numpy(graph, 1 / int(lam_max))

    top_katz = sorted(
        node_values.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    highest_katz = [i[0] for i in top_katz]
    return (highest_katz * num_rounds)


def mixed_strategy(graph, num_seeds, num_rounds):
    closeness = closeness_strategy(graph, num_seeds, int(num_rounds / 2))
    eigen = eigenvector_strategy(graph, num_seeds, int(num_rounds / 2))

    return closeness + eigen


def dominating_set_strategy(G, num_seeds, num_rounds):
    dominating_set = list(nx.dominating_set(G))

    # Obtaining seeds nodes from selecting the highest deg from the dominating
    seeds = []
    degrees = G.degree(dominating_set)
    i = 0
    for k in sorted(degrees, key=lambda k: k[1], reverse=True):
        seeds.append(k[0])
        i += 1
        if i >= num_seeds:
            break

    # if the size of dominating set is smaller than num of seed, randomly
    # select
    if len(seeds) < num_rounds:
        remaining_nodes = list(G.nodes())
        for node in dominating_set:
            if node in remaining_nodes:
                remaining_nodes.remove(node)
        np.random.shuffle(remaining_nodes)
        for i in range(num_rounds - len(seeds)):
            seeds.append(remaining_nodes[i])
    return seeds * num_rounds


def load_centraility(G, num_rounds, num_seeds):
    load_dic = nx.load_centrality(G)
    top_load = sorted(
        load_dic.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    highest_load = [i[0] for i in top_load]
    return (highest_load * num_rounds)


def subgraph_centraility(G, num_rounds, num_seeds):
    centrality = nx.subgraph_centrality(G)
    top_nodes = sorted(
        centrality.items(), key=operator.itemgetter(1),
        reverse=True)[:num_seeds]
    highest_nodes = [i[0] for i in top_nodes]
    return (highest_nodes * num_rounds)


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
    # strategy = eigenvector_strategy(G, num_seeds, num_rounds)
    # strategy = dominating_set_strategy(G, num_seeds, num_rounds)
    # strategy = load_centraility(G, num_seeds, num_rounds)
    # strategy = mixed_strategy(G, num_seeds, num_rounds)
    strategy = closeness_strategy(G, num_seeds, num_rounds)

    # Save input file
    save_output(output_filename, strategy)
