bp=int(input("enter basic payment of the employee:"))
d=input("enter designation of the employee:")
if(bp<40000 and d=="ADMIN"):
    if bp*0.12>2500:
        print("bonus pay for the employee:",bp*0.12)
    else:
        print("bonus pay can not be less than of 2500")
elif(bp>=40000 and d=="MANAGER"):
    if bp*0.16<7500:
        print("bonus pay for the employee:",bp*0.16)
    else:
        print("bonus pay should not be more than 7500")
elif(bp<20000 and d=="OFFICER"):
    if bp*0.12>1500:
        print("bonus pay for the employee:",bp*0.12)
    else:
        print("bonus pay can not be less than of 1500")
    
else:
    print("bonus pay for the employee:",bp*0.089)

