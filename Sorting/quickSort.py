# __author__ = Vishu Kamble
"""
A python program to perform quicksort
"""


def quickSort(arr):
    helper_func(arr, 0, len(arr) - 1)


def helper_func(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        helper_func(arr, first, splitpoint - 1)
        helper_func(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivot = arr[first]

    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and arr[left] <= pivot:
            left = left + 1

        while arr[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return right

arr = [54, 23, 45, 12, 59, 29, 10, 4, 2, 1, 43]
quickSort(arr)
print arr
