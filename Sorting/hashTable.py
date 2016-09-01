class hashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):

        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.data[hashvalue] = data
            self.slots[hashvalue] = key

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                nextslot = self.rehash(hashvalue, self.slots)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))  # Go through list finding empty slot

                if self.slots[nextslot] is None:    # found next slot which is empty. Fill it
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data  # replace data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        pos = startslot

        while self.slots is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]

            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


h = hashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'

print h[1]
print h[2]
print h[4]

