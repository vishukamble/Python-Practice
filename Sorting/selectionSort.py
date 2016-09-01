# __author__ = Vishu Kamble
"""
A python program to perform selection sort
"""

def selectionSort(arr):
    for slot in range(len(arr)-1, 0, -1):
        maxPos = 0
        for location in range(1, slot+1):
            if arr[location] > arr[maxPos]:
                maxPos = location

        temp = arr[slot]
        arr[slot] = arr[maxPos]
        arr[maxPos] = temp

arr = [32,1,56,23,12, 9, 20]
selectionSort(arr)
print arr
