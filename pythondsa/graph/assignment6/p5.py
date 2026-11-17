m = int(input()) 
if m <= 0:
    raise SystemExit("Table size must be greater than 0.")
keys = list(map(int, input().split())) 
t = [None]*m 
for k in keys: 
    if k in t:
        continue
    done = False 
    for i in range(m): 
        j = (k % m + i*i) % m 
        if t[j] is None: 
            t[j] = k; done = True; break 
    if not done: print("Could not insert", k) 
print("Quadratic probing table:") 
for i, v in enumerate(t): print(i, ":", v if v is not None else "Empty")