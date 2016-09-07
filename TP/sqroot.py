# __author__ = Vishu Kamble
"""
A python program to find square root of integer rounded to nearest int without sqrt()
"""


def root(num):
    if num < 0:
        return ValueError

    if num == 1:
        return 1

    low = 0
    high = num/2

    while low+1 < high:
        mid = low + (high-low)/2
        sq = mid ** 2

        if sq == num:
            return mid
        elif sq < num:
            low = mid
        else:
            high = mid

    return low


print root(48)
