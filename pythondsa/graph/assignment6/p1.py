def digit_hash(k, m): 
    return sum(int(x) for x in str(abs(k))) % m 
  
m = int(input()) 
if m <= 0:
    raise SystemExit("Table size must be greater than 0.")
keys = list(map(int, input().split())) 
a, b = [0]*m, [0]*m 
print("Key Division DigitSum") 
for k in keys: 
    x, y = k % m, digit_hash(k, m) 
    a[x] += 1; b[y] += 1 
    print(k, x, y) 
print("Division distribution:", a) 
print("Digit-sum distribution:", b)