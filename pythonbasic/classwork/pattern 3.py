n=int(input("enter no. of rows"))
for i in range(1,n+1,2):
    for j in range(i,n,2):
        print(" ",end="")
    for k in range(1, i+1,2):
        print("*",end="")
    for l in range(i,n,2):
        print(" ",end="")
    print()