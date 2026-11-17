# Read hash table size (m) and the keys to insert
m = int(input())
keys = list(map(int, input().split()))

# Initialize hash table with separate chaining (list of lists)
table = [[] for _ in range(m)]

# Insert keys into the hash table
for key in keys:
    index = key % m
    table[index].append(key)

# Print the hash table contents
print("Hash Table (Separate Chaining):")
for i, chain in enumerate(table):
    print(i, ":", " -> ".join(map(str, chain)) if chain else "None")

# Search for a target key in the hash table
target = int(input())
index = target % m

if target in table[index]:
    print("Key", target, "found at index", index)
else:
    print("Key", target, "not found")