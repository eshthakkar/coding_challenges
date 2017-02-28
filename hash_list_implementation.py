class HashTable(object):
    """ Implement a Hashtable using 2 lists, one to hold the keys and another one to hold the data corresponding to it"""

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def hashfunction(self, key, size):
        """ Calculates and returns the position where the key and data should be stored in the hash table"""

        return key % size


    def rehash(self, oldhash, size):
        """ Calculates a new hash value using the old collided hash value and returns it"""
        
        return (oldhash + 1) % size  


    def put(self, key, data):
        """ Add a key-data pair into the hash table"""

        position = self.hashfunction(key, len(self.slots))

        # key not present in the hash table, adding it to the hash table
        if self.slots[position] is None:
            self.slots[position] = key
            self.data[position] = data

        # key already present in the hash table, in that case just update its value    
        elif self.slots[position] == key:
            self.data[position] = data  

        # in case of a collision    
        else:
            next_slot = self.rehash(position,len(self.slots))

            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot,len(self.slots))

            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data


    def get(self,key):
        """ Get the value corresponding to a key from the hash table"""

        found = False
        stop = False
        data = None

        start_position = self.hashfunction(key, len(self.slots))
        position = start_position

        while self.slots[position] != None and not found and not stop:

            # key is found at the start hash value
            if self.slots[position] == key:
                found = True
                data = self.data[position] 

            else:
                position = self.rehash(position,len(self.slots))
                if position == start_position:
                    stop = True 

        return data   


    def __getitem__(self,key):
        return self.get(key) 


    def __setitem__(self,key,data):
        self.put(key,data)                      


# Testing

h = HashTable()
h[34] = "cat"
h[55] = "dog"
h[77] = "panda"
h[44] = "duck"

print h.slots
print h.data

h.put(90,"human")

print h.slots
print h.data

h.put(80,"human")

print h.slots
print h.data

h.put(81,"human")

print h.slots
print h.data

h.put(82,"human")

print h.slots
print h.data

h.put(83,"human")

print h.slots
print h.data

h.put(84,"human")

print h.slots
print h.data

h.put(85,"human")

print h.slots
print h.data

print h.get(91)
print h.slots
print h.data

print h[-999]
print h[55]




              
          


