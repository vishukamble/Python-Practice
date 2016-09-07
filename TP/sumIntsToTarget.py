# __author__ = Vishu Kamble
"""
A python program to check if two integers in list of integers can sum up to the target value
"""


def sumInts(lst, target):
    seen = set()

    for num1 in lst:
        num2 = target - num1  # 5 + 3 = 8, so 3 = 8 - 5

        if num2 in seen:
            return True

        seen.add(num1)

    return False


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print sumInts(arr, 9)