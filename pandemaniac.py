import sys
import json
import numpy as np
import networkx as nx

from operator import itemgetter

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
    print(highest_degree)
    return highest_degree * num_rounds

def generate_degree(graph, num_seeds, num_rounds):
    degree_list = []
    new_nodes = nx.degree_centrality(graph)
    for node in range(num_seeds):
        degree_list.append((node, new_nodes[str(node)]))
    degree_list.sort(key = itemgetter(1), reverse = True)

    new_deg_list = [i[0] for i in degree_list]
    return new_deg_list * num_rounds

def generate_betweenness(graph, num_seeds, num_rounds):
    betweenness_list = [0 for i in range(num_seeds + 1)]
    new_nodes = nx.betweenness_centrality(graph, k=len(graph)/10)
    for node in range(num_seeds):
        betweenness_list.append((node, new_nodes[str(node)]))
    betweenness_list.sort(key = itemgetter(1), reverse = True)

    new_bet_list = [i[0] for i in betweenness_list]
    return new_bet_list * num_rounds

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
    strategy = generate_degree(G, num_seeds, num_rounds)

    # Save input file
    save_output(output_filename, strategy)
