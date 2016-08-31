# __author__ = Vishu Kamble
"""
A python program to computer all permutations of string
"""

def permutation(s):
    result = []
    if len(s) == 1:
        return s

    else:
        for x, letter in enumerate(s):
            print "Letter", letter
            for perm in permutation(s[:x] + s[x+1:]):
                result += [letter+perm]
                print result

        return result

print permutation('abc')
