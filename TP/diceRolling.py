# __author__ = Vishu Kamble
"""
A python program to perform a dice roll and reroll if value > 5
"""

from random import randint


def roll():
    return randint(1,7)


def converto5():
    dice = 7
    while dice > 5:
        dice = roll()
        print "Roll produced ", dice

    print "Result : ",dice

converto5()