def check(s):
    for i in s[0:25]:
        c=0
        print(i)
        if i=='@':
            c=c+1
    if(c==0):
        print("@ is absent")
    else:
        print("@ is present")
    print("no. of @ is:",c)
sen=input("enter a sentence:")
check(sen)