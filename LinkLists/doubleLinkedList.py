# __author__ = Vishu Kamble
"""
A python program to implement basic doublylinkedlist
"""

class doublyLinkedList(object):
    def __init__(self, data):
        self.value = data
        self.nextnode = None
        self.prevnode = None


a = doublyLinkedList(1)
b = doublyLinkedList(2)
c = doublyLinkedList(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b

print a.value
print b.value
print b.nextnode.value  # value of c
print b.prevnode.value  #value of a
print c.prevnode.value  #value of b