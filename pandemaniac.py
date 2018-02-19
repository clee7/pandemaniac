import sys
import json
import numpy as np
import networkx as nx

def load_graph(filename):
    # Get the adjacency list
    with open(filename) as f:
        graph = json.load(f)
    return graph


def generate_random(nodes, num_seeds):
    random_list = []
    np.random.shuffle(nodes)
    for i in range(num_seeds):
        random_list.append(nodes[i])

    return random_list

def generate_degree(graph, node, num_seeds):
    degree_list = []
    new_nodes = nx.degree_centrality(graph)
    for node in num_seeds:
        degree_list.append((node, new_nodes[node]))

    degree_list.sort(key = itemgetter(1), reverse = True)
    return degree_list

def generate_betweenness(graph, nodes, num_seeds):
    betweenness_list = []
    new_nodes = nx.betweenness_centrality(graph, k=len(graph)/10)
    for node in num_seeds:
        betweenness_list.append((node, new_nodes[node]))
    betweenness_list.sort(key = itemgetter(1), reverse = True)

    return betweenness_list

def save_output(filename, strategies, num_rounds):

    file = open(filename, "w")
    for i in range(num_rounds):
        for j in range(len(strategies)):
            file.writelines(str(strategies[j]) + '\n')
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python pandemaniac.py <path_to_json_file>")
        sys.exit(1)

    filename = sys.argv[1]

    nums = filename.split('.')
    num_players = int(nums[0])
    num_seeds = int(nums[1])
    num_rounds = 50

    # Get the adjacency list
    graph = load_graph(filename)

    # Get the list of nodes
    nodes = list(graph.keys())

    # Create graph
    G = nx.from_dict_of_lists(nodes)

    # Generate a list of random nodes as root nodes
    # strategies = generate_random(nodes, num_seeds)
    strategies = generate_degree(G, nodes, num_seeds)

    # Save input file
    output_filename = filename.rsplit('.', 1)[0] + ".txt"
    save_output(output_filename, strategies, num_rounds)
