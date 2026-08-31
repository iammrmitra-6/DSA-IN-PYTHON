n=int("enter no of terms")
if n<=0:
    print(0)
elif n == 1:
    print(1)
else:
    print(1,",")
    print(0,",")
    for i in range(2,n):
        print()
