# This file contains the sorting algorithms


# Performs the insertion sort algorithm on the given array
def insertion_sort(array):
    for j in range(1, array.size):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key


# Performs the quick sort algorithm on the given array
def quick_sort(array, start, end):
    if start < end:
        q = partition(array, start, end)
        quick_sort(array, start, q - 1)
        quick_sort(array, q + 1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start - 1

    for p in range(start, end):
        if array[p] <= pivot:
            array[p], array[i] = array[i], array[p]
            i = i + 1

    array[end], array[i + 1] = array[i + 1], array[end]
    return i + 1



