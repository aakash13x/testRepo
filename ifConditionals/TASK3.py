#Check if triangle and find the type

def checkType(num1,num2,num3):
    if(num1==num2==num3):
        print("The triangle is EQUILATERAL")
    elif(num1==num2 or num2==num3 or num3==num1):
        print("The triangle is ISOSCELES")
    else:
        print("The triangle is OBTUSE")

x = int(input("Enter side 1: "))
y = int(input("Enter side 2: "))
z = int(input("Enter side 3: "))

if(x<y+z and y < x+z and z < x+y):
    checkType(x,y,z)
else:
    print("It is not a triangle.")
