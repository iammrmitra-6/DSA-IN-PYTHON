n=int(input("enter a number"))
t=n**2
s=0
while t>0:
    d=t%10
    s=s+d
    t=t//10
if s==n:
    print("neon number")
else:
    print("not a neon number")