n=int(input("enter the last term:"))
x=int(input("enter the value of x:"))
s=0
for i in range(1,n+1):
    s=s+(x**i/i)
print(s)