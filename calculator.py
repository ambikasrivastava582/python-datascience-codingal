# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def sub(x, y):
    return x - y

# This function multiplies two numbers
def mul(x, y):
    return x * y

# This function divides two numbers
def div(x, y):
    return x / y

num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Number 2"))

print("Sum :", add(num1, num2))
print("Difference :", sub(num1, num2))
print("Product :", mul(num1, num2))
print("Quotient :", div(num1, num2))