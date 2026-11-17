m = int(input()) 
if m <= 1:
    raise SystemExit("Table size must be a prime number greater than 1.")
if any(m % divisor == 0 for divisor in range(2, int(m**0.5) + 1)):
    raise SystemExit("Table size must be a prime number greater than 1.")
keys = list(map(int, input().split())) 
t = [None]*m 
for k in keys: 
    if k in t:
        continue
    h1 = k % m 
    h2 = 1 + (k % (m-1)) 
    placed = False 
    for i in range(m): 
        j = (h1 + i*h2) % m 
        if t[j] is None: 
            t[j] = k; placed = True; break 
    if not placed: print("Could not insert", k) 
print("Double hashing table:") 
for i, v in enumerate(t): print(i, ":", v if v is not None else "Empty")