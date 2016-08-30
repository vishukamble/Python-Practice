# __author__ = Vishu Kamble
"""
A python program to implement bult in Queue functions using list
"""

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, num):
        self.items.insert(0, num)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print q.isEmpty()
for i in range(5):
    q.enqueue(i)
print "Size: ", q.size()
print q.isEmpty()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.isEmpty()