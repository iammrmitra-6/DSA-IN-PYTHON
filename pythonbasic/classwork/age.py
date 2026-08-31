age=int(input("Enter the age of the person :"))
gender=input("enter your gender :")

if gender =="female":
    print("she will work only in urban areas")

elif gender=="male" and age>=20 and age<=40:
    print("he may work in anywhere")

elif gender=="male" and age>40 and age<=60:
    print("he will work in urban area only")

else:
    print("error")