# __author__ = Vishu Kamble
"""
A python program to implement bult in stack functions using list
"""

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, num):
        self.items.append(num)

    def pop(self):
        return self.items.pop()

    def peek(self):
        l = len(self.items) - 1  #indexing starts at 0, so lenght -1 will be top
        return self.items[l]

    def size(self):
        return len(self.items)


s = Stack()
print s.isEmpty()
s.push(1)
s.push("2")
s.push(3)
print "Size: ", s.size()
print s.isEmpty()
print "Top: ", s.peek()
print s.pop()
print s.pop()
print s.pop()
print s.isEmpty()