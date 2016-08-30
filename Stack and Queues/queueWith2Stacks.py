# __author__ = Vishu Kamble
"""
A python program to implement queue using 2 stacks
"""

class queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, num):
        self.stack1.append(num)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                pop = self.stack1.pop()
                self.stack2.append(pop)
        return self.stack2.pop()

q = queue2Stacks()
print "Adding elements 1 to 5"
for i in range(5):
    q.enqueue(i)

print "Removing elements 1 to 5 in FIFO"
for i in range(5):
    print q.dequeue()