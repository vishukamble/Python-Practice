# __author__ = Vishu Kamble
"""
A python program to find how many times a character is repeated in string
"""

def compressed(str):
    length = len(str)
    counts = dict()
    for i in range(length):
        counts[str[i]] = counts.get(str[i], 0) + 1

    for key,value in counts.items():
        print key, value


compressed("AAAABBBCCCCCDDDD")