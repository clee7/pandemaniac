import sys
import json
import numpy as np


def load_graph(filename):
    # Get the adjacency list
    with open(filename) as f:
        graph = json.load(f)
    return graph


def parse_file_path(file_path):
    parts = path.rsplit('/', 1)
    directory = ""
    filename = parts[0]
    if len(parts) >= 2:
        directory = parts[0] + "/"
        filename = parts[1]
    nums = filename.split('.')
    num_players = int(nums[0])
    num_seeds = int(nums[1])
    return (directory, filename, num_players, num_seeds)


def generate_random(nodes, num_seeds, num_rounds):
    # Get the list of nodes
    nodes = list(graph.keys())

    # Select random from nodes
    random_list = []
    np.random.shuffle(nodes)
    for i in range(num_seeds):
        random_list.append(nodes[i])
    return random_list * num_rounds


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

    # Generate a list of random nodes as root nodes
    strategy = generate_random(graph, num_seeds, num_rounds)

    # Save input file
    save_output(output_filename, strategy)
