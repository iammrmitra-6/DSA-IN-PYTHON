m = int(input()) 
if m <= 0:
    raise SystemExit("Table size must be greater than 0.")
keys = list(map(int, input().split())) 
table = [[] for _ in range(m)] 
for k in keys: 
    table[k % m].append(k) 
  
x = int(input("Search key: ")) 
print("Search:", "Found" if x in table[x % m] else "Not found") 
y = int(input("Delete key: ")) 
if y in table[y % m]: 
    table[y % m].remove(y); print("Deleted") 
else: print("Key not found") 
for i, bucket in enumerate(table): 
    print(i, ":", bucket if bucket else "Empty")