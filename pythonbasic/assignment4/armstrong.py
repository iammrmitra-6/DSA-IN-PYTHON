n=int(input("enter a number"))
t=n
i=len(str(n))
s=0
while t>0:
    d=t%10
    s=s+d**i
    t=t//10
if n==s:
    print("armstrong number")
else:
    print("not a armstrong number")
