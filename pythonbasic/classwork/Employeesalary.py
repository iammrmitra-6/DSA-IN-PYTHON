basic_pay = float(input("Enter the basic pay: "))
designation = input("Enter the designation (Admin / Manager / Officer / Other): ").strip().lower()

bonus = 0

if designation == "admin":
    bonus = 0.12 * basic_pay
    if bonus < 2500:
        bonus = 2500

elif designation == "manager":
    bonus = 0.16 * basic_pay
    if bonus > 7500:
        bonus = 7500

elif designation == "officer":
    bonus = 0.14 * basic_pay
    if bonus < 1500:
        bonus = 1500
    elif bonus > 2500:
        bonus = 2500

else:
    bonus = 0.089 * basic_pay

print("Festival Bonus = Rs.", bonus)
