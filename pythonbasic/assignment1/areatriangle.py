import math
a=int(input("enter first side of the triangle:"))
b=int(input("enter second side of the triangle:"))
c=int(input("enter third side of the triangle"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of the triangle :",s)
