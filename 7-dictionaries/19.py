string = input("Enter string: ")
print(dict([char, string.count(char)] for char in string))