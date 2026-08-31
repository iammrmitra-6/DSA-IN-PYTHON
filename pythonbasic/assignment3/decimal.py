n=int(input("enter a number:"))
t=n
b=0
while t!=0:
    d=t%2
    b=str(d)+b
    t=t//2
print(b)
