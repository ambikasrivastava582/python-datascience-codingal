text = input("Enter a word or sentence: ")
ch = input("Enter the character to search: ")

count = 0
i = 0

while i < len(text):
    if text[i] == ch:
        count += 1
    i += 1

if count > 0:
    print("Character found", count, "time(s)")
else:
    print("Character not found")
