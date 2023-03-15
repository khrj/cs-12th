def even(lst):
    return [num for num in lst if num % 2 == 0]


print(even([int(x) for x in input("Enter numbers separated by commas: ").split(",")]))
