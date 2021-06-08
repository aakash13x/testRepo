'''2.1 single if to determine odd or even

x = int(input("Enter the integer: "))

if(x%2 == 0):
    print("The integer is even.")

else:
    print("The integer is odd.")

#2.2 rectangle or square

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

if(length == breadth):
    print("It is a square.")
else:
    print("It is a rectangle.")
'''

#2.3 greatest of two int

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

if(a > b):
    print(a,"is greater.")
elif(b>a):
    print(b,"is greater.")
else:
    print("They are equal.")
