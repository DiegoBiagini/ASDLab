import pickle
from timeit import default_timer as timer

import matplotlib.pyplot as plt

from randomarrays import *
from sorting import *


def main():
    # Maximum allowed time for an execution : 3 minutes
    max_time = 180
    results = []
    save = True

    # Insertion sort

    results = test_sorting(max_time, insertion_sort, get_random_nodup, save, "data/insertion_rand")
    print("Insertion sort su array casuale:\n", results)
    plot_and_save("Insertion sort casuale", results)

    results = test_sorting(10, insertion_sort, get_random_asc, save, "data/insertion_best")
    print("Insertion sort su array crescente(best case):\n", results)
    plot_and_save("Insertion sort best case", results)

    results = test_sorting(max_time, insertion_sort, get_random_desc, save, "data/insertion_worst")
    print("Insertion sort su array decrescente(worst case):\n", results)
    plot_and_save("Insertion sort worst case", results)

    # Quick sort

    results = test_sorting(max_time, quick_sort, get_random_nodup, save, "data/quick_rand")
    print("Quicksort su array casuale:\n", results)
    plot_and_save("Quick sort casuale", results)

    results = test_sorting(max_time, quick_sort, get_quick_best_case, save, "data/quick_best")
    print("Quicksort su array apposito(best case):\n", results)
    plot_and_save("Quick sort best case", results)

    results = test_sorting(max_time, insertion_sort, get_random_desc, save, "data/quick_worst")
    print("Quicksort su array crescente(worst case):\n", results)
    plot_and_save("Quick sort worst case", results)

    # Both
    results = test_both(max_time, save)
    print("Insertion sort e quicksort su stesso array:\n", results, save)
    plot_and_save_both("Insertion sort e Quicksort casuale",results)


# Function that dictates the growth of the array size
def next_size(current_size):
    return current_size * 2


# Standard test function, takes the max time the test is allowed to run, the sorting algorithm that will be used and
# the function that will generate the array of values
# puts into the list passed as a parameters the tuples: (size, time)
# If save_to_file is true saves the various array to file
def test_sorting(max_time, sorting_f, random_array_f, save_to_file, filename):
    results = []
    current_size = 1
    sorting_time = 0

    try:
        while sorting_time < max_time:

            # Create next array
            current_size = next_size(current_size)
            rand_array = random_array_f(current_size)
            if save_to_file:
                with open(filename + "_" + str(current_size) + "_in.dat","wb") as f:
                    pickle.dump(results, f)

            sorting_time = timer()
            sorting_f(rand_array)
            sorting_time = timer() - sorting_time

            results.append((current_size, sorting_time))
    except RecursionError:
        pass
    if save_to_file:
        with open(filename + "_out.dat", "wb") as f:
            pickle.dump(results, f)
    return results


# Tests both insertion and quick on the same random arrays
# puts into the list passed as a parameters the tuples: (size, time_insertion, time_quicksort)
def test_both(max_time, save_to_file):
    results = []
    current_size = 1
    bigger_time = 0

    try:
        while bigger_time < max_time:

            # Create next array
            current_size = next_size(current_size)
            rand_array = get_random_nodup(current_size)
            if save_to_file:
                with open("data/both_sort_" + str(current_size) + "_in.dat", "wb") as f:
                    pickle.dump(results, f)

            insertion_time = timer()
            insertion_sort(rand_array.copy())
            insertion_time = timer() - insertion_time

            quick_time = timer()
            quick_sort(rand_array.copy())
            quick_time = timer() - quick_time

            bigger_time = max(insertion_time, quick_time)

            results.append((current_size, insertion_time, quick_time))
    except RecursionError:
        pass
    if save_to_file:
        with open("data/both_sort_out.dat", "wb") as f:
            pickle.dump(results, f)
    return results


def plot_and_save(title, results):
    plt.clf()

    plt.plot([rec[0] for rec in results], [rec[1] for rec in results])
    plt.xlabel("Size")
    plt.ylabel("Time(s)")

    title = ''.join(x for x in title.title() if not x.isspace())
    plt.savefig("../plots/" + title + ".png")


def plot_and_save_both(title, results):
    plt.clf()

    plt.plot([rec[0] for rec in results], [rec[1] for rec in results], label="InsertionSort")
    plt.plot([rec[0] for rec in results], [rec[2] for rec in results], label="QuickSort")

    plt.xlabel("Size")
    plt.ylabel("Time(s)")
    plt.legend()

    title = ''.join(x for x in title.title() if not x.isspace())
    plt.savefig("../plots/" + title + ".png")


if __name__ == '__main__':
    main()

