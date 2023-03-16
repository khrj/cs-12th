def split_tuple(tup):
    print(tup[:len(tup) // 2])
    print(tup[len(tup) // 2:])


split_tuple(input("Enter values separated by commas: ").split(","))
