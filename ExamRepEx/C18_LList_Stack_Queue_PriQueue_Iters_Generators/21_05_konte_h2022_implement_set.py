# Define the default hash-table size 
 
DEFAULT_INITIAL_CAPACITY = 4 
 
# Define default load factor 
DEFAULT_MAX_LOAD_FACTOR = 0.75 
 
# Define the maximum hash-table size to be 2 ** 30 
MAXIMUM_CAPACITY = 2 ** 30 
 
 
class Set: 
    def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold=DEFAULT_MAX_LOAD_FACTOR): 
        # Current hash-table capacity. Capacity is a power of 2 
        self.capacity = capacity 
 
        # Specify a load factor used in the hash table 
        self.loadFactorThreshold = loadFactorThreshold 
 
        # Create a list of empty buckets 
        self.table = [] 
        for i in range(self.capacity): 
            self.table.append([]) 
 
        self.size = 0  # Initialize set size 
 
    # Add an entry (key, value) into the map 
    def add(self, key): 
        if self.size >= self.capacity * self.loadFactorThreshold: 
            if self.capacity == MAXIMUM_CAPACITY: 
                raise RuntimeError("Exceeding maximum capacity") 
 
            self.rehash() 
 
        bucketIndex = self.getHash(hash(key)) 
 
        # Add an entry (key, value) to hashTable[index] 
        if not (key in self.table[bucketIndex]): 
            self.table[bucketIndex].append(key) 
            self.size += 1  # Increase size 
 
    # Remove the entry for the specified key 
    def remove(self, key): 
        bucketIndex = self.getHash(hash(key)) 
 
        # Remove the first entry that matches the key from a bucket 
        if len(self.table[bucketIndex]) > 0: 
            bucket = self.table[bucketIndex] 
            for e in bucket: 
                if e == key: 
                    bucket.remove(e) 
                    self.size -= 1  # Decrease size 
                    break  # Remove just one entry that matches the key 
 
    # Return true if the specified key is in the map 
    def contains(self, key): 
        if self.get(key) != None: 
            return True 
        else: 
            return False 
 
    # Return the first value that matches the specified key 
    def get(self, key): 
        bucketIndex = self.getHash(hash(key)) 
        if len(self.table[bucketIndex]) > 0: 
            bucket = self.table[bucketIndex] 
            for e in bucket: 
                if e == key: 
                    return e 
 
        return None 
 
    # Return all keys in a list 
    def keys(self): 
        keys = [] 
 
        for i in range(self.capacity): 
            if len(self.table[i]) > 0: 
                bucket = self.table[i] 
                for e in bucket: 
                    keys.append(e) 
 
        return keys 
 
    # Return a string representation for the keys in this set 
    def __str__(self): 
        return str(self.keys()) 
 
    # Remove all of the entries from this map 
    def clear(self): 
        self.size = 0  # Reset map size 
 
        self.table = []  # Reset map 
        for i in range(self.capacity): 
            self.table.append([]) 
 
    # Return the number of mappings in this map 
    def getSize(self): 
        return self.size 
 
    # Return true if this map contains no entries 
    def isEmpty(self): 
        return self.size == 0 
 
    # Rehash the map 
    def rehash(self): 
        temp = self.keys()  # Get elements 
        self.capacity *= 2  # Double capacity 
        self.table = []  # Create a new hash table 
        self.size = 0  # Clear size 
        for i in range(self.capacity): 
            self.table.append([]) 
 
        for e in temp: 
            self.add(e)  # Store to new table 
 
    # Return the hash table as a string 
    def getTable(self): 
        return str(self.table) 
 
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold): 
        self.loadFactorThreshold = threshold 
 
    def supplementalHash(self, h): 
        h ^= (h >> 20) ^ (h >> 12) 
        return h ^ (h >> 7) ^ (h >> 4) 
 
    def getHash(self, hashCode): 
        return self.supplementalHash(hashCode) & (self.capacity - 1)
    
     # The union, difference, and intersect methods are left as exercise
     
    def union(self, other):
        result_set = Set()
        for k in self.keys():
            result_set.add(k)
        
        other_keys = other.keys()
        
        for k in other_keys:
            if not result_set.contains(k):
                result_set.add(k)
        return result_set
    
    def difference(self,other):
        result_set = Set()
        other_keys = other.keys()
        
        for k in self.keys():
            if not k in other_keys: # all values in keys not in other
                result_set.add(k)
        return result_set
    
    
    def intersection(self,other):
        result_set = Set()
        other_keys = other.keys()
        
        for k in self.keys():
            if k in other_keys:
                result_set.add(k)
        return result_set
    
    def symmetric_difference(self, other):# all values not common among s1 and s2
        result_set = Set()
        other_keys = other.keys()
        
        total_size = self.getSize() + other.getSize()
        
        for k in self.keys():
            if k not in other_keys: # all values in keys not in other
                result_set.add(k)
                print(k)
                
        for e in other.keys():
            if e not in self.keys(): # all values in other not in keys
                result_set.add(e)
                print(e)
        
        return result_set
        
    

s1 = Set() 
s1.add(1) 
s1.add(2) 
s1.add(4)
 
s2 = Set() 
s2.add(1) 
s2.add(3) 
s2.add(5) 
# sUnion = s1.union(s2) 
# print("Union", sUnion) 
# sDiff = s1.difference(s2) 
# print("Difference", sDiff) 
# sIntersect = s1.intersection(s2) 
# print("Intersect", sIntersect) 
s_symDif = s1.symmetric_difference(s2)
print("Symmetric difference:", s_symDif)