import networkx as nx
import numpy as np


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
