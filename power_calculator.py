base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Answer =", result)
