string = input("Enter string: ")

stack = []

for char in string:
    stack.append(char)

reverse = ""

while True:
    try:
        character = stack.pop()
        reverse += character
    except:
        break


print(reverse == string)
