
#ejercicio 2 del capitulo 11


import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.displaced = []

    def digit_folding(self, key, group_size):
        key_str = str(key)
        groups = [key_str[i:i+group_size] for i in range(0, len(key_str), group_size)]
        return sum([int(group) for group in groups])

    def linear_probe(self, key):
        i = 0
        while True:
            idx = (self.digit_folding(key, 3) + i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                break
            else:
                i += 1
        if idx != self.digit_folding(key, 3):
            self.displaced.append(key)

    def quadratic_probe(self, key):
        i = 0
        while True:
            idx = (self.digit_folding(key, 2) + i**2) % self.size
            if self.table[idx] is None:
                self.table[idx] = key
                break
            else:
                i += 1
        if idx != self.digit_folding(key, 2):
            self.displaced.append(key)

    def find_displaced_keys(self):
        return self.displaced

# Generar 1000 números enteros aleatorios de 10 dígitos
keys = random.sample(range(10000000000), 1000)

# Initialize hash tables with size 103
sizes = [103] * 2
tables = [HashTable(size) for size in sizes]

# Inserción de claves en tablas hash mediante sondas lineales y cuadráticas
for table in tables:
    for key in keys:
        if table is tables[0]:
            table.linear_probe(key)
        else:
            table.quadratic_probe(key)

# Encontrar claves desplazadas y mostrar recuentos para cada esquema de sonda y factor de carga
load_factors = [0.5, 0.7, 0.9]
probe_schemes = ['linear', 'quadratic']
for i, table in enumerate(tables):
    print(f"Probe scheme: {probe_schemes[i]}")
    for factor in load_factors:
        max_keys = int(table.size * factor)
        displaced_keys = table.find_displaced_keys()[:max_keys]
        print(f"Load factor: {factor}")
        print(f"Number of displaced keys: {len(displaced_keys)}")
