# This file contains functions that generate random arrays with certain properties
import random


# Creates an array of the given size and fills it with pseudo random values between a min and max value(both included)
def random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


# Creates an array of the given size and fills it with values between 0 and size-1 in ascending order
def random_asc_order(size):
    return [i for i in range(0, size)]


# Creates an array of the given size and fills it with values between 0 and size-1 in descending order
def random_desc_order(size):
    return [size - i - 1 for i in range(0, size)]


# Creates an array of the given size and fills it with random values between 0 and size-1 with a single
# occurrence per value
def random_single_occurrence(size):
    random_asc = random_asc_order(size)

    # Randomize in place
    for i in range(0, size):
        rand_index = random.randint(i, size - 1)
        random_asc[i], random_asc[rand_index] = random_asc[rand_index], random_asc[i]

    return random_asc
