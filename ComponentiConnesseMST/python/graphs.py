import random

import numpy as np


# Create a random directed graph with n nodes and randomly connects it
# p is the probability that an arc will be activated
def create_digraph(n, p):
    graph = np.zeros((n, n))

    with np.nditer(graph, op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1):
                x[...] = 1

    return graph


# Create a random weighted directed graph with n nodes and randomly connects it
# p is the probability that an arc will be activated, min and max are the bounds for the weights
def create_weighted_digraph(n, p, min, max):
    graph = np.zeros((n, n))

    with np.nditer(graph, op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1):
                x[...] = random.randint(min, max)

    return graph


# Create a random graph with n nodes and randomly connects it
# p is the probability that an arc will be activated
def create_graph(n, p):
    graph = np.zeros((n, n))

    with np.nditer(graph, flags=['multi_index'], op_flags=['readwrite']) as it:
        while not it.finished:
            index = it.multi_index
            if index[0] <= index[1]:
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
            if index[0] <= index[1]:
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
