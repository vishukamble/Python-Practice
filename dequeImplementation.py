class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, item):
        pass

    def addFront(self, num):
        self.items.append(num)

    def addRear(self, num):
        self.items.insert(0, num)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Deque()
print "Is queue empty: ",q.isEmpty()
for i in range(3):
    q.addFront(i)
for i in range(4,7):
    q.addRear(i)

print "Size: ", q.size()
print "Is queue empty: ",q.isEmpty()

print q.removeFront(), ' ' , q.removeRear()