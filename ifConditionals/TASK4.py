price = int(input("Enter the cost of the product: "))
quantity = int(input("Enter the number of products: "))

amount = price * quantity

if(amount > 1000):
    payableAmount = amount - (amount/10)
    print("You got a discount!")
    print("The total cost is", payableAmount)

else:
    print("The total cost is",amount)
