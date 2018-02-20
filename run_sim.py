import pandemaniac as pd
import dominating_set as ds
import sim
import sys
import networkx as nx

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python pandemaniac.py <path_to_json_file>")
        sys.exit(1)

    path = sys.argv[1]

    # Define global var
    num_rounds = 50

    # Parse the input path to find filename and number of players and seeds
    (directory, filename, num_players, num_seeds) = pd.parse_file_path(path)

    graph = pd.load_graph(path)

    # Generate graph from nodes
    G = nx.from_dict_of_lists(graph)

    # Generate a list of random nodes as root nodes
    # random_nodes = pd.random_nodes_strategy(graph, num_seeds, num_rounds)
    # highest_degree = pd.highest_degree_strategy(G, num_seeds, num_rounds)
    between = pd.betweenness_strategy(G, num_seeds, num_rounds)
    # dominating = ds.dominating_set_strategy(G, num_seeds, num_rounds)
    # eigenvector_strat = pd.eigenvector_strategy(G, num_seeds, num_rounds)
    # closeness_strat = pd.closeness_strategy(G, num_seeds, num_rounds)

    # random_nodes = random_nodes[:num_seeds]
    # highest_degree = highest_degree[:num_seeds]
    between = between[:num_seeds]
    # dominating = dominating[:num_seeds]
    # eigenvector_strat = eigenvector_strat[:num_seeds]
    # closeness_strat = closeness_strat[:num_seeds]

    # 2.10.11
    strat = between
    TA_degree = [106, 7, 122, 60, 18, 30, 44, 53, 128, 66]

    print("TA_degree", TA_degree)
    print("our strat", strat)
    nodes = {"our": strat, "TA_degree": TA_degree}
    result = sim.run(graph, nodes)
    print(result)
