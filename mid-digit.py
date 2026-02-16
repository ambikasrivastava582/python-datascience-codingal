num = input("Enter a number: ")
length = len(num)
product = 1

for i in range(length):
    if length % 2 == 1 and i == length//2:
        product = product * int(num[i])
    elif length % 2 == 0 and (i == length//2 or i == length//2 - 1):
        product = product * int(num[i])

print("Middle product =", product)
