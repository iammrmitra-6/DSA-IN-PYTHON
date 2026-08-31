s=1
q=1
n=int(input("enter a number to be converted into binary:"))
while(n<0):
    s=n%2
    print(s)
    q=n/2
    n=q