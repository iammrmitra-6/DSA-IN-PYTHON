marks=int(input("enter marks of the student out of 100:"))
if (marks>=90):
    print("grade is outstanding")
elif(marks>=80 and marks<90):
    print("grade is excellent")
elif(marks>=70 and marks<80):
    print("grade is average")
elif(marks>=40 and marks<70):
    print("grade is pass")
else:
    print("grade is fail")
