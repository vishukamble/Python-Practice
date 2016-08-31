# __author__ = Vishu Kamble
"""
A python program to show recursion
"""


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

print reverse('Hello World')