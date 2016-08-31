# __author__ = Vishu Kamble
"""
A python program to calculate factorial using recursion
"""

def fact(n):
    if n == 0:
        return 1

    else:
        return n*fact(n-1)

print fact(5)
print fact(6)
print fact(7)