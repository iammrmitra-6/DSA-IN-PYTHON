EMPTY, DELETED = None, "DELETED" 
m = int(input())  
if m <= 0:
    raise SystemExit("Table size must be greater than 0.")
keys = list(map(int, input().split())) 
t = [EMPTY]*m 
  
def find(k): 
    for i in range(m): 
        j = (k+i) % m 
        if t[j] is EMPTY: return -1 
        if t[j] == k: return j 
    return -1 
  
for k in keys: 
    if find(k) >= 0:
        continue
    for i in range(m): 
        j = (k+i) % m 
        if t[j] is EMPTY or t[j] == DELETED: 
            t[j] = k; break 
    else:
        print("Could not insert", k)
  
x = int(input("Search key: ")) 
print("Search index:", find(x)) 
y = int(input("Delete key: ")) 
p = find(y) 
if p >= 0: t[p] = DELETED; print("Deleted") 
else: print("Not found") 
print("Final table:", t)