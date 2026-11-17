m = int(input()) 
if m <= 0:
    raise SystemExit("Table size must be greater than 0.")
keys = list(map(int, input().split())) 
t = [None]*m 
for k in keys: 
    if k in t:
        continue
    placed = False
    for i in range(m): 
        j = (k+i) % m 
        if t[j] is None:
            t[j] = k
            placed = True
            break
    if not placed:
        print("Could not insert", k)
  
def probes(k): 
    count = 0 
    for i in range(m): 
        count += 1 
        j = (k+i) % m 
        if t[j] is None or t[j] == k: return count 
    return count 
  
a = int(input("Present key: ")) 
b = int(input("Absent key: ")) 
print("Load factor:", round(sum(value is not None for value in t)/m, 2)) 
print("Successful probes:", probes(a)) 
print("Unsuccessful probes:", probes(b))