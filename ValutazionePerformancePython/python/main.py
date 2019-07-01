from randomarrays import *
from sorting import *
from timeit import default_timer as timer


def main():
    # Maximum allowed time for an execution : 3 minutes
    print(get_quick_best_case(7))



# Function that dictates the growth of the array size
def next_size(current_size):
    return current_size * 2


# Standard test function, takes the max time the test is allowed to run, the sorting algorithm that will be used and
# the function that will generate the array of values
# it return a list of tuples: (size, time)
def test_sorting(max_time, sorting_f, random_array_f):
    current_size = 1
    sorting_time = 0
    results = []

    while sorting_time < max_time:

        # Create next array
        current_size = next_size(current_size)
        rand_array = random_array_f(current_size)

        sorting_time = timer()
        sorting_f(rand_array)
        sorting_time = timer() - sorting_time

        results.append({current_size, sorting_time})

    return results


# Tests both insertion and quick on the same random arrays
# returns a list of tuples like this: (size, time_insertion, time_quicksort)
def test_both(max_time):
    current_size = 1
    both_timer = 0
    results = []

    while both_timer < max_time:

        both_timer = timer()

        # Create next array
        current_size = next_size(current_size)
        rand_array = get_random_nodup(current_size)

        insertion_time = timer()
        insertion_sort(rand_array)
        insertion_time = insertion_time - timer()

        quick_time = timer()
        quick_sort(rand_array)
        quick_time = timer() - quick_time

        both_timer = timer() - both_timer

        results.append({current_size, insertion_time, quick_time})

    return results


if __name__ == '__main__':
    main()

