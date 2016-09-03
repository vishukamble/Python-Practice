# __author__ = Vishu Kamble
"""
A python program to perform binary search
"""


def binarySearch(arr, value):
    low = 0
    high = len(arr) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) / 2
        if mid == value:
            found = True
        else:
            if value < mid:
                high = mid - 1
            else:
                low = mid + 1

    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print binarySearch(arr, 4)
