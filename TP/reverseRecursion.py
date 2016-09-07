# __author__ = Vishu Kamble
"""
A python program to reverse string using recursion
"""

def reverse(s):
    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]

print reverse('Vishu')