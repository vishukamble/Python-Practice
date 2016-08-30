# __author__ = Vishu Kamble
"""
A python program to find which number is missing in array using zip
"""

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

print finder([1,2,3,4,5,6], [1,3,4,5,6])