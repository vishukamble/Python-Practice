# __author__ = Vishu Kamble
"""
A python program to perform insertion sort
"""

def insertion(arr):

    for i in range(1,len(arr)):
        curr_value = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > curr_value:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = curr_value

    print arr

arr = [54, 23,45,12,59, 29, 10, 4, 2, 1, 43]
insertion(arr)
