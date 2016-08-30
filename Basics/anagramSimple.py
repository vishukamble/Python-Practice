# __author__ = Vishu Kamble
"""
A python program to check if two strings are anagrams
"""

def anagram(str1, str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ', '').lower()
    if sorted(str1) == sorted(str2):
        print str1 + " and " + str2 + " are anagrams"

    else:
        print str1 + " and " + str2 + " are not anagrams"

anagram('god', 'dog')