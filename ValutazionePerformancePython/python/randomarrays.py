# This file contains functions that generate random arrays with certain properties
import random


# Creates an array of the given size and fills it with pseudo random values between a min and max value(both included)
def get_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


# Creates an array of the given size and fills it with values between 0 and size-1 in ascending order
def get_random_asc(size):
    return [i for i in range(0, size)]


# Creates an array of the given size and fills it with values between 0 and size-1 in descending order
def get_random_desc(size):
    return [size - i - 1 for i in range(0, size)]


# Creates an array of the given size and fills it with random values between 0 and size-1 with a single
# occurrence per value
def get_random_nodup(size):
    random_asc = get_random_asc(size)

    # Randomize in place
    for i in range(0, size):
        rand_index = random.randint(i, size - 1)
        random_asc[i], random_asc[rand_index] = random_asc[rand_index], random_asc[i]

    return random_asc
