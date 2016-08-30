# __author__ = Vishu Kamble
"""
A python program to find if string has alll the unique characters
"""

def unichar(s):
    return len(set(s)) == len(s)

print unichar('abcdef')
print unichar('abcdefdsa')