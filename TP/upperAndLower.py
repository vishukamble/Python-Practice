# __author__ = Vishu Kamble
"""
A python program to count number of upper case characters and lower case
"""

def findUpperLower(s):

    d = {"upper": 0, "lower": 0}

    for letter in s:
        if letter.isupper():
            d["upper"] += 1
        elif letter.islower():
            d["lower"] += 1
        else:
            pass # blank spaces

    print "String: ", s
    print "Upper characters: ", d["upper"]
    print "Lower characters: ", d["lower"]


s = "Hello, Hi, How're you doing?"
findUpperLower(s)