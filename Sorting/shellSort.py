# __author__ = Vishu Kamble
"""
A python program to perform shell sort
"""

def shell(arr):
    sublist = len(arr)/2

    while sublist > 0:
        for start in range(sublist):
            gap_insert(arr, start, sublist)

        print "after increment of size: ", sublist
        print "list is: ", arr

        sublist = sublist / 2


def gap_insert(arr, start, gap):

    for i in range(start+gap, len(arr), gap):
        curr_value = arr[i]
        pos = i

        while pos >= gap and arr[pos-gap] > curr_value:

            arr[pos] = arr[pos-gap]
            pos = pos - gap

        arr[pos] = curr_value

arr = [54, 23,45,12,59, 29, 10, 4, 2, 1, 43]
shell(arr)