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
    highest_degree = pd.highest_degree_strategy(G, num_seeds, num_rounds)
<<<<<<< HEAD
    # between = pd.betweenness_strategy(G, num_seeds, num_rounds)
    dominating = ds.dominating_set_strategy(G, num_seeds, num_rounds)
=======
    eigenvector_strat = pd.eigenvector_strategy(G, num_seeds, num_rounds)
    closeness_strat = pd.closeness_strategy(G, num_seeds, num_rounds)
    between = pd.betweenness_strategy(G, num_seeds, num_rounds)
>>>>>>> 8a8b6b36cdd1e423169a76cf67a44a9e02f43fab

    # random_nodes = random_nodes[:num_seeds]
    highest_degree = highest_degree[:num_seeds]
<<<<<<< HEAD
    # between = between[:num_seeds]
    dominating = dominating[:num_seeds]

    nodes = {"highest degree": highest_degree, "dominating": dominating}
=======
    eigenvector_strat = eigenvector_strat[:num_seeds]
    closeness_strat = closeness_strat[:num_seeds]

    nodes = {"degree": highest_degree, "eigen": eigenvector_strat}
>>>>>>> 8a8b6b36cdd1e423169a76cf67a44a9e02f43fab
    result = sim.run(graph, nodes)
    print(result)
