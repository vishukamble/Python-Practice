# __author__ = Vishu Kamble
"""
A python program to check if two strings are anagrams using dictionary and get method
"""

def anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if len(str1) != len(str2):
        return False

    count = {}
    for letter in str1:
        count[letter] = count.get(letter, 0) + 1  # checks if key exists, if yes increments counter, else creates key

    for letter in str2:
        count[letter] = count.get(letter, 0) - 1

    for k in count:
        if count[k] != 0:
            return False

    return True

print anagram('god', 'dogdsa')