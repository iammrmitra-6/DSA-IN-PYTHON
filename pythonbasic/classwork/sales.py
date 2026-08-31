salesA=int(input("enter sales in region A:"))
salesB=int(input("enter sales in region B:"))
if(salesA<15000):
    print("commission is nil")
elif(salesB<15000 and salesA<16000):
    print("commission is :",0.065*(salesA+salesB))
elif((salesB+salesA)>=15000 and salesB<25000 and salesA>=16000 and salesA<35000):
    print("commission is :",0.085*(salesA+salesB)+1500)
else:
    print("commission is :",0.11*(salesA+salesB)+4500)