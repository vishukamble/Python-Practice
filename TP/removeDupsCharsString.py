# __author__ = Vishu Kamble
"""
A python program to remove duplicate characters in string
"""


def removeDups(s):
    result = []
    occured = set()

    for i in s:
        if i not in occured:
            occured.add(i)
            result.append(i)

    print ''.join(result)


removeDups('Jack Sparrow')
