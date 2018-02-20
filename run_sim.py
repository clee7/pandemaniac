import pandemaniac as pd
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
    random_nodes = pd.random_nodes_strategy(graph, num_seeds, num_rounds)
    highest_degree = pd.highest_degree_strategy(graph, num_seeds, num_rounds)
    between = pd.betweenness_strategy(G, num_seeds, num_rounds)
    dominating = pd.dominating_set_strategy(G, num_seeds, num_rounds)
    eigenvector_strat = pd.eigenvector_strategy(G, num_seeds, num_rounds)
    closeness_strat = pd.closeness_strategy(G, num_seeds, num_rounds)
    katx_strat = pd.katz_strategy(G, num_seeds, num_rounds)
    load_strat = pd.load_centraility(G, num_seeds, num_rounds)
    subgraph = pd.subgraph_centraility(G, num_seeds, num_rounds)
    neighbor_degree = pd.neighbor_highest_degree(graph, num_seeds, num_rounds)
    mixed_strat = pd.mixed_strategy(G, num_seeds, num_rounds)

    random_nodes = random_nodes[:num_seeds]
    highest_degree = highest_degree[:num_seeds]
    between = between[:num_seeds]
    dominating = dominating[:num_seeds]
    eigenvector_strat = eigenvector_strat[:num_seeds]
    closeness_strat = closeness_strat[:num_seeds]
    katx_strat = katx_strat[:num_seeds]
    load_strat = load_strat[:num_seeds]
    subgraph = subgraph[:num_seeds]
    neighbor_degree = neighbor_degree[:num_seeds]
    mixed_strat = mixed_strat[:num_seeds]
    print("eigen: ", eigenvector_strat)

    strat = [random_nodes, highest_degree, between, dominating,
             eigenvector_strat, closeness_strat, katx_strat, load_strat,
             subgraph, neighbor_degree, mixed_strat]

    # day1/2.10.10.json --> eigen, closeness, katx, subgraph
    # TA = [75, 1, 70, 77, 90, 39, 87, 20, 64, 215]

    # day1/2.10.20.json -->
    # highest_deg, eigen, closeness, katx, subgraph, neighbor
    # TA = [49, 59, 57, 148, 135, 10, 107, 77]

    # day2/2.10.11.json --> neighbor_degree
    TA = [106, 7, 122, 60, 18, 30, 44, 53, 128, 66]

    # day2/2.10.21.json --> closeness_strat
    # TA = [189, 164, 130, 87, 80, 165, 183, 93]

    score = []

    for strati in strat:
        # print("TA_degree", TA_degree)
        # print("our strat", strati)
        nodes = {"our": strati, "TA": TA}
        result = sim.run(graph, nodes)
        # print(result)
        score.append(result)

    print(score)
