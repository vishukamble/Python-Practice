# __author__ = Vishu Kamble
"""
A python program to implement single linkedlist
"""

class Node(object):
    def __init__(self, data):
        self.value = data
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print a.value
print b.value
print b.nextnode.value