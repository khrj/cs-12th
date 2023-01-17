string = input("Enter string: ")
print({char: string.count(char) for char in string if char.isalpha()})
