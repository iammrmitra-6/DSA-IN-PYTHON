def insert(table, key, method):
    m = len(table)
    for i in range(m):
        h1 = key % m
        if method == "linear":
            index = (h1 + i) % m
        elif method == "quadratic":
            index = (h1 + i * i) % m
        else:  # double hashing
            h2 = 1 + (key % (m - 1))
            index = (h1 + i * h2) % m
            
        if table[index] is None:
            table[index] = key
            return True
            
    return False

# Read hash table size (m) and the keys to insert
m = int(input())
keys = list(map(int, input().split()))

# Test different probing methods
for method in ("linear", "quadratic", "double"):
    table = [None] * m
    for key in keys:
        if not insert(table, key, method):
            print(method.title(), ": table full; could not insert", key)
    print(method.title(), "Probing:", table)