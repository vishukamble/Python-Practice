# __author__ = Vishu Kamble
"""
A python program to check if string is palindrome
"""

def palindrome(s):
    return s == s[::-1]

print palindrome("Hello")
print palindrome("abcba")