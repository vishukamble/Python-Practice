# __author__ = Vishu Kamble
"""
A python program to calculate fibonacci series
"""

def fibonacci(num):
    if num == 0 or num == 1:
        return num

    else:
        return fibonacci(num-1) + fibonacci(num-2)


print fibonacci(10)