l=[10,23,45,67,98,56,34,53]
c,v=0,0
for el in l:
    if(el%2==0):
        c+=1
    else:
        v+=1
print("no of even & odd:",c,v)