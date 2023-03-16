(lst := input("Enter list separated by commas: ").split(',')) and print(set([x for x in lst if lst.count(x) == 3]))
