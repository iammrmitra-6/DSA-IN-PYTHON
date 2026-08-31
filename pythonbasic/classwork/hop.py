l=list(eval(input("enter a list of number:")))
res=abs(l[1]-l[0])
n=len(l)
for i in range(n-1):
    res=max(res,abs(l[i]-l[i+1]))
    i+=1
print(res)

