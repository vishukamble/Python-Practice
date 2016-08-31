# __author__ = Vishu Kamble
"""
A python program that prints the nth to last node given by user
"""

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n - 1):
        if not right_pointer.nextnode:
            raise LookupError("N is larger than linked list")

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer

class Node(object):
    def __init__(self, data):
        self.value = data
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

x = nth_to_last_node(2, a)
print x.value
