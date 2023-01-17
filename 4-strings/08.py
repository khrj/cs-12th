digits = [int(x) for x in filter(lambda x: x.isdigit(), input("Enter string: "))]
print(sum(digits))