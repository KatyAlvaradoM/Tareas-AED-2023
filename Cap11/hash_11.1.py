import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.displaced = []

    def hash_func(self, key):
        return key % self.size

    def linear_probe(self, key):
        i = 0
        while True:
            idx = (self.hash_func(key) + i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                break
            else:
                i += 1
        if idx != self.hash_func(key):
            self.displaced.append(key)

    def quadratic_probe(self, key):
        i = 0
        while True:
            idx = (self.hash_func(key) + i**2) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                break
            else:
                i += 1
        if idx != self.hash_func(key):
            self.displaced.append(key)

    def double_hash_probe(self, key):
        i = 0
        while True:
            h1 = self.hash_func(key)
            h2 = 1 + (key % (self.size - 1))
            idx = (h1 + i * h2) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                break
            else:
                i += 1
        if idx != self.hash_func(key):
            self.displaced.append(key)

    def find_displaced_keys(self):
        return self.displaced

# Generate 200 random integers in the range [0, 999]
keys = random.sample(range(1000), 200)

# Initialize hash tables with size 103
sizes = [103] * 9
tables = [HashTable(size) for size in sizes]

# Insert keys into hash tables using linear, quadratic, and double hash probes
for i, table in enumerate(tables):
    for key in keys:
        if i % 3 == 0:
            table.linear_probe(key)
        elif i % 3 == 1:
            table.quadratic_probe(key)
        else:
            table.double_hash_probe(key)

# Find displaced keys and show counts for each probe scheme and load factor
load_factors = [0.5, 0.7, 0.9]
probe_schemes = ['linear', 'quadratic', 'double hash']
for i, table in enumerate(tables):
    print(f"Probe scheme: {probe_schemes[i%3]}")
    for j, factor in enumerate(load_factors):
        max_keys = int(table.size * factor)
        displaced_keys = table.find_displaced_keys()[:max_keys]
        print(f"Load factor: {factor}")
        print(f"Number of displaced keys: {len(displaced_keys)}")
