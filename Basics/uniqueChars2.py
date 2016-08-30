# __author__ = Vishu Kamble
"""
A python program to find if string has alll the unique characters
"""

def unichar(s):
    char = set()
    for letter in s:
        if letter in char:
            return False
        else:
            char.add(letter)

    return True

print unichar("abcde")
print unichar("abcdedasda")