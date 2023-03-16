lst = [int(x) for x in input("Enter list of numbers separated by commas: ").split(",")]
print("Even:", [x for x in lst if x % 2 == 0], "\nOdd:", [x for x in lst if x % 2 != 0])
