print(len(t1 := input("Enter first tuple separated by commas: ").split(',')) == len([x for x in input("Enter second tuple separated by commas: ").split(",") if x in t1]))
