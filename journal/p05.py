string = input("Enter string: ")
indexes = []

for i, char in enumerate(string):
    if char == "a":
        indexes.append(i)

print(indexes)