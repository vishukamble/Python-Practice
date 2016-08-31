# __author__ = Vishu Kamble
"""
A python program to calculate sum using recursion
"""

def recursiveSum(n):
    if n == 0:
        return 0
    else:
        return n + recursiveSum(n-1)

print recursiveSum(33)  # 561