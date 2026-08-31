n=int(input("enter a number"))
t=n
s=0
while t>0:
    d=t%10
    s=s+d
    t=t//10
if n%s==0:
    print("niven number")
else:
    print("not a niven number")