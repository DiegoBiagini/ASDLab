from enum import Enum

import numpy as np

# Costs of the various operations, they can't be negative
COPYC = 0
REPLACEC = 1
DELETEC = 1
INSERTC = 1
TWIDDLEC = 2


# Enum for the operations on characters
class Op(Enum):
    NULL = 0
    COPY = 1
    REPLACE = 2
    DELETE = 3
    INSERT = 4
    TWIDDLE = 5


# Algorithm
def edit_distance_matrix(x, y):
    m = len(x)
    n = len(y)

    # Initialize matrices
    c = np.zeros((m + 1, n + 1))
    op = np.zeros((m + 1, n + 1))

    for i in range(0, m + 1):
        c[i, 0] = i * DELETEC
        op[i, 0] = Op.DELETE.value

    for j in range(0, n + 1):
        c[0, j] = j * INSERTC
        op[0, j] = Op.INSERT.value

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Index in the string
            r_i = i - 1
            r_j = j - 1

            mincost = np.inf
            minop = Op.NULL.value

            # Copy
            if x[r_i] == y[r_j]:
                mincost = c[i-1, j-1] + COPYC
                minop = Op.COPY

            # Replace
            if x[r_i] != y[r_j] and c[i-1, j-1] + REPLACEC < mincost:
                mincost = c[i-1, j-1] + REPLACEC
                minop = Op.REPLACE

            # Twiddle
            if i >= 2 and j >= 2 and x[r_i] == y[r_j-1] and y[r_j] == x[r_i-1] and c[i-2, j-2] + TWIDDLEC < mincost:
                mincost = c[i-2, j-2] + TWIDDLEC
                minop = Op.TWIDDLE

            # Delete
            if c[i-1, j] + DELETEC < mincost:
                mincost = c[i-1, j] + DELETEC
                minop = Op.DELETE

            # Insert
            if c[i, j-1] + INSERTC < mincost:
                mincost = c[i, j-1] + INSERTC
                minop = Op.INSERT

            c[i, j] = mincost
            op[i, j] = minop.value

    return c, op


# Only returns the edit distance
def edit_distance(x, y):
    c, op = edit_distance_matrix(x, y)
    return c[len(x), len(y)]


# Finds the closest word using simple edit distance
# Takes the word to examine and a list of words(dictionary)
# Returns the closest word and its distance from the query
def closest_word(word, dictionary):
    mindistance = np.Inf
    closest = ""

    for entry in dictionary:
        distance = edit_distance(word, entry)
        if distance < mindistance:
            mindistance = distance
            closest = entry

    return closest, mindistance

