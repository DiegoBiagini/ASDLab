from randomarrays import *
from sorting import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def main():
    # Maximum allowed time for an execution : 3 minutes
    max_time = 5
    results = []

    # Insertion sort
    test_sorting(max_time, insertion_sort, get_random_nodup, results)
    print("Insertion sort su array casuale:\n", results)
    plot_and_save("Insertion sort casuale", results)

    test_sorting(max_time, insertion_sort, get_random_asc, results)
    print("Insertion sort su array crescente(best case):\n", results)
    plot_and_save("Insertion sort best case", results)

    test_sorting(max_time, insertion_sort, get_random_desc, results)
    print("Insertion sort su array decrescente(worst case):\n", results)
    plot_and_save("Insertion sort worst case", results)

    # Quick sort
    test_sorting(max_time, quick_sort, get_random_nodup, results)
    print("Quicksort su array casuale:\n", results)
    plot_and_save("Quick sort casuale", results)

    test_sorting(max_time, quick_sort, get_quick_best_case, results)
    print("Quicksort su array apposito(best case):\n", results)
    plot_and_save("Quick sort best case", results)

    test_sorting(max_time, insertion_sort, get_random_desc, results)
    print("Quicksort su array crescente(worst case):\n", results)
    plot_and_save("Quick sort worst case", results)
    
    # Both
    test_both(max_time, results)
    print("Insertion sort e quicksort su stesso array:\n", results)
    plot_and_save_both("Insertion sort e Quicksort casuale",results)


# Function that dictates the growth of the array size
def next_size(current_size):
    return current_size * 2


# Standard test function, takes the max time the test is allowed to run, the sorting algorithm that will be used and
# the function that will generate the array of values
# puts into the list passed as a parameters the tuples: (size, time)
def test_sorting(max_time, sorting_f, random_array_f, results):
    results.clear()
    current_size = 1
    sorting_time = 0

    try:
        while sorting_time < max_time:

            # Create next array
            current_size = next_size(current_size)
            rand_array = random_array_f(current_size)

            sorting_time = timer()
            sorting_f(rand_array)
            sorting_time = timer() - sorting_time

            results.append((current_size, sorting_time))
    except RecursionError:
        pass
    return results


# Tests both insertion and quick on the same random arrays
# puts into the list passed as a parameters the tuples: (size, time_insertion, time_quicksort)
def test_both(max_time, results):
    results.clear()
    current_size = 1
    bigger_time = 0

    try:
        while bigger_time < max_time:

            # Create next array
            current_size = next_size(current_size)
            rand_array = get_random_nodup(current_size)

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
    return results


def plot_and_save(title, results):
    plt.clf()

    plt.plot([rec[0] for rec in results], [rec[1] for rec in results])
    plt.suptitle(title)
    plt.xlabel("Size")
    plt.ylabel("Time(s)")

    title = ''.join(x for x in title.title() if not x.isspace())
    plt.savefig("../plots/" + title + ".png")


def plot_and_save_both(title, results):
    plt.clf()

    plt.plot([rec[0] for rec in results], [rec[1] for rec in results], label="InsertionSort")
    plt.plot([rec[0] for rec in results], [rec[2] for rec in results], label="QuickSort")

    plt.suptitle(title)
    plt.xlabel("Size")
    plt.ylabel("Time(s)")
    plt.legend()

    title = ''.join(x for x in title.title() if not x.isspace())
    plt.savefig("../plots/" + title + ".png")


if __name__ == '__main__':
    main()

