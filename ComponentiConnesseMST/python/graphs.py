import random

import numpy as np


# Create a random graph with n nodes and randomly connects it
# p is the probability that an arc will be activated
def create_graph(n, p):
    graph = np.zeros((n, n))

    with np.nditer(graph, op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1):
                x[...] = 1

    return graph


# Create a random weighted graph with n nodes and randomly connects it
# p is the probability that an arc will be activated, min and max are the bounds for the weights
def create_weighted_graph(n, p, min, max):
    graph = np.zeros((n, n))

    with np.nditer(graph, op_flags=['readwrite']) as it:
        for x in it:
            if p > random.uniform(0, 1):
                x[...] = random.randint(min, max)

    return graph

