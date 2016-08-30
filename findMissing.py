# __author__ = Vishu Kamble
"""
A python program to find which number is missing in array
"""


def finder(arr1, arr2):
    l = max(len(arr1), len(arr2))
    for i in range(l):
        if arr1[i] not in arr2:
            print arr1[i]

finder([1,2,3,4,5,6], [1,3,4,5,6])