import random

import numpy as np

from set import *


# Create a random directed graph with n nodes and randomly connects it
# p is the probability that an arc will be activated
def create_digraph(n, p):
    graph = np.zeros((n, n))

    with np.nditer(graph, flags=['multi_index'], op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1) and it.multi_index[0] != it.multi_index[1]:
                x[...] = 1

    return graph


# Create a random weighted directed graph with n nodes and randomly connects it
# p is the probability that an arc will be activated, min and max are the bounds for the weights
def create_weighted_digraph(n, p, min, max):
    graph = np.zeros((n, n))

    with np.nditer(graph, op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1) and it.multi_index[0] != it.multi_index[1]:
                x[...] = random.randint(min, max)

    return graph


# Create a random graph with n nodes and randomly connects it
# p is the probability that an arc will be activated
def create_graph(n, p):
    graph = np.zeros((n, n))

    with np.nditer(graph, flags=['multi_index'], op_flags=['readwrite']) as it:
        while not it.finished:
            index = it.multi_index
            if index[0] < index[1]:
                if p > random.uniform(0, 1):
                    graph[index] = 1
                    graph[(index[1], index[0])] = 1
            it.iternext()

    return graph


# Create a random weighted graph with n nodes and randomly connects it
# p is the probability that an arc will be activated, min and max are the bounds for the weights
def create_weighted_graph(n, p, min, max):
    graph = np.zeros((n, n))

    with np.nditer(graph, flags=['multi_index'], op_flags=['readwrite']) as it:
        while not it.finished:
            index = it.multi_index
            if index[0] < index[1]:
                if p > random.uniform(0, 1):
                    rand_number = random.randint(min, max)
                    graph[index] = rand_number
                    graph[(index[1], index[0])] = rand_number
            it.iternext()

    return graph


# Returns a list of all nodes adjacent to the one passed as argument(nodes are identified by the row they appear in the
# adjacency matrix
def adjacent_nodes(graph, node):
    adj = []
    row = graph[node, ...]

    i = 0
    for element in row:
        if element != 0:
            adj.append(i)
        i += 1

    return adj


# Finds the connected components of a non directed graph
# Returns a list of lists, each list is a connected component and it contains the nodes in the CC
def connected_components(graph):
    n = graph.shape[0]
    sets = []
    for i in range(0, n):
        sets.append(make_set(i))

    with np.nditer(graph, flags=['multi_index']) as it:
        while not it.finished:
            u = it.multi_index[0]
            v = it.multi_index[1]

            if it.value != 0:
                if find_set(sets[u]) != find_set(sets[v]):
                    union(sets[u], sets[v])

            it.iternext()

    final_list = []
    all_repr = []
    for cc in sets:
        if cc.representative not in all_repr:
            final_list.append(set_to_list(cc))
            all_repr.append(cc.representative)

    return final_list


# Returns a list of tuples, each tuple contains the arc weight and a tuple with the nodes it connects
def get_arcs_list(graph):
    list = []
    with np.nditer(graph, flags=['multi_index']) as it:
        while not it.finished:
            u = it.multi_index[0]
            v = it.multi_index[1]

            if it.value != 0 and u <= v:
                list.append((it.value, it.multi_index))

            it.iternext()

    return list


# Returns a list of tuples which represents the arcs in ascending order, for non directed graphs
def order_arcs(graph):
    arcs = get_arcs_list(graph)
    arcs.sort(key=lambda x: x[0])
    return arcs


# Executes the Kruskal algorithm to find MST of a connected graph
# Returns a list of arcs which represent the MST of the given graph
def kruskal_algorithm(graph):
    MST = []
    # Check if the graph is connected
    ccs = connected_components(graph)
    if len(ccs) > 1:
        return []

    # Make sets for each node
    n = graph.shape[0]
    sets = []
    for i in range(0, n):
        sets.append(make_set(i))

    ordered_arcs = order_arcs(graph)

    for arc in ordered_arcs:
        u = arc[1][0]
        v = arc[1][1]
        if find_set(sets[u]) != find_set(sets[v]):
            MST.append(arc)
            union(sets[u], sets[v])

    return MST