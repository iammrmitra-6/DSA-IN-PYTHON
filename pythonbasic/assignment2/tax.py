income = int(input("Enter income: ")) 
if income <= 250000: 
    print("No tax") 
elif income <= 500000: 
    print("Tax =", (income - 250000) * 0.05) 
elif income <= 1000000: 
    print("Tax =", 12500 + (income - 500000) * 0.20) 
else: 
    print("Tax =", 112500 + (income - 1000000) * 0.30)