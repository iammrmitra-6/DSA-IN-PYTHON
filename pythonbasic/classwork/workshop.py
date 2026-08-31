hrs=int(input("enter the number of hours you worked :"))

if hrs<=37:
    print("your payment is :",23*hrs)

elif hrs>37 and hrs<=65:
    p=hrs-37
    print("your payment is :",37*23+31*p)
else:
    q=hrs-65
    print('your payment',37*23+28*31+q*41) 