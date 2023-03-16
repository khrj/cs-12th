lst = input("Enter list separated by commas: ").split(",")
print([item for item in lst if lst.count(item) == 1])