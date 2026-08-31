cls=int(input("enter the total number of classes :"))
atd=int(input("enter the total number of classes attended:"))

pt=(atd/cls)*100

if pt>=75:
    print("student is allowed to sit in the exam")

else:
    print("student is not allowed to sit in exam.")