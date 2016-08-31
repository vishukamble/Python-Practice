# __author__ = Vishu Kamble
"""
A python program to implement circular linkedlist
"""

class circulatLinkedList(object):
    def __init__(node):
        marker1 = node
        marker2 = node

        while marker2 != None and marker2.nextnode != None:
            marker1 = marker1.nextnode
            marker2 = marker2.nextnode.nextnode

            if marker2 == marker1:
                return True

        return False

class Node(object):
    def __init__(self, data):
        self.value = data
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a

x = circulatLinkedList()
print x