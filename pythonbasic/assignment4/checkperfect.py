n=int(input("enter a numnber"))
t=n
s=0
for i in range (1,n):
    if n%i==0:
        s=s+i
print(s)
if (s==n):
    print("perfect")
else :
    print("not a perfect number")