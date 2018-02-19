import networkx as nx
import operator

def eigenvector_strategy(graph, num_seeds, num_rounds):
	highest_eigenvectors = []
	node_values = nx.eigenvector_centrality(graph)

	top_eigenvalues = sorted(node_values.items(), key = operator.itemgetter(1), reverse = True)[:num_seeds]
	highest_eigenvectors = [i[0] for i in top_eigenvalues]
	return (highest_eigenvectors * num_rounds)

def closeness_strategy(graph, num_seeds, num_rounds):
	highest_closeness = []
	node_values = nx.closeness_centrality(graph)
	top_closeness = sorted(node_values.items(), key = operator.itemgetter(1), reverse = True)[:num_seeds]
	highest_closeness = [i[0] for i in top_closeness]
	return (highest_closeness * num_rounds)