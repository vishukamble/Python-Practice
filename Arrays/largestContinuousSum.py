# __author__ = Vishu Kamble
"""
A python program to find the largest continuous sum in array
"""

def largest_sum(arr):
    if len(arr) == 0:
        return

    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print largest_sum([1,2,3,4,5,6,3,2,1,7,8])
