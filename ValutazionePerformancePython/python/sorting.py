# This file contains the sorting algorithms


# Performs the insertion sort algorithm on the given array
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1

        array[i + 1] = key


# Performs the quick sort algorithm on the given array
def quick_sort(array):
    quick_sort_rec(array, 0, len(array) - 1)


def quick_sort_rec(array, start, end):
    if start < end:
        q = partition(array, start, end)
        quick_sort_rec(array, start, q - 1)
        quick_sort_rec(array, q + 1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start - 1

    for p in range(start, end):
        if array[p] <= pivot:
            i = i + 1
            array[p], array[i] = array[i], array[p]

    array[end], array[i + 1] = array[i + 1], array[end]
    return i + 1



