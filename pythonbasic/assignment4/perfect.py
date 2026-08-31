
def perfect(n):
    t=n
    s=0
    for i in range (1,n):
        if n%i==0:
            s=s+i
    return s==n
p=0
for num in range(1,1001):
    if perfect(num):
        print(num)

