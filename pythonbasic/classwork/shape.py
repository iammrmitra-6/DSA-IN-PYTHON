a=int(input("Enter length of the first side of the shape"))
b=int(input("Enter length of the second side of the shape"))
c=int(input("Enter breadth of the third side of the shape"))
d=int(input("Enter breadth of the fourth side of the shape"))
angle=int(input("Enter one of the internal angle of the shape"))
if(a==c==b==d and angle==90):
    print("shape is square")
elif(a==c==b==d and angle!=0):
    print("shape is rhombus")
elif(a==b and c==d and angle==90):
    print("shape is rectangle")
elif(a==b and c==d and angle!=90):
    print("shape is parallelogram")
else:
    print("shape is irregular")