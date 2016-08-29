import ctypes

# __author__ = Vishu Kamble
"""
A python program to create dynamic arrays with built in functions
"""

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError('K out of bounds!')

        return self.A[item]

    def append(self, value):
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = value
        self.n += 1

    def _resize(self, new_capacity):

        B = self.make_array(new_capacity)
        for item in range(self.n):
            B[item] = self.A[item]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capactiy):
        return (new_capactiy * ctypes.py_object)()


arr = DynamicArray()
arr.append('1')
print len(arr)

arr.append('2')
print len(arr)

print arr[0]
