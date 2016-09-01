# __author__ = Vishu Kamble
"""
A python program to perform sequential search
"""


def sequential(arr, value):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == value:
            found = True
        else:
            pos += 1

    return found


### if input array is ordered / sorted ###
def sequentialOrdered(arr, value):
    pos = 0
    found = False
    stop = False

    while pos < len(arr) and not found and not stop:
        if arr[pos] == value:
            found = True
        else:
            if arr[pos] > value:
                stop = True
            else:
                pos += 1

    return found

arr = [1, 3, 5, 7, 8, 10, 12, 33, 43, 58, 69,78, 99]
print sequential(arr, 43)
print sequentialOrdered(arr, 43)
