def factorial(j):
    f=1
    for i in range(1,j+1):
        f=f*i
    return(f)

n=int(input("enter the last term:"))
x=int(input("enter the value of x:"))
s=0
for i in range(1,n+1):
    s=s+(x**i/factorial(i))
print(s)