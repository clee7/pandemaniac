import sys
import json
import numpy as np


def load_graph(filename):
    # Get the adjacency list
    with open(filename) as f:
        graph = json.load(f)
    return graph


def generate_random(nodes, num_of_root_nodes):
    random_list = []
    np.random.shuffle(nodes)
    for i in range(num_of_root_nodes):
        random_list.append(nodes[i])

    return random_list


def save_output(filename, strategies, num_rounds):

    file = open(filename, "w")
    for i in range(num_rounds):
        for j in range(len(strategies)):
            file.writelines(str(strategies[j]) + '\n')
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python pandemaniac.py <path_to_json_file> <num_nodes>")
        sys.exit(1)

    filename = sys.argv[1]
    total_nodes = int(sys.argv[2])

    num_rounds = 50
    num_root = int(total_nodes / num_rounds)

    # Get the adjacency list
    graph = load_graph(filename)

    # Get the list of nodes
    nodes = list(graph.keys())

    # Generate a list of random nodes as root nodes
    strategies = generate_random(nodes, num_root)

    # Save input file
    output_filename = filename.rsplit('.', 1)[0] + ".txt"
    save_output(output_filename, strategies, num_rounds)
