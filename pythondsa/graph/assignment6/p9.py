symbols = {} 
n = int(input()) 
for _ in range(n): 
    name, typ = input().split() 
    if name in symbols:
        print("Duplicate:", name)
    else:
        symbols[name] = typ
q = input("Search identifier: ") 
if q in symbols: 
    print(q, "has type", symbols[q]) 
else: 
    print("Identifier not declared") 
print("Symbol Table:") 
for name, typ in symbols.items(): 
    print(name, ":", typ)