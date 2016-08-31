# __author__ = Vishu Kamble
"""
A python program to calculate sum of digits using recursion
"""


def digitsum(n):
    if n < 10:
        return n

    else:
        return n % 10 + digitsum(n / 10)


print digitsum(321332)  # 14
