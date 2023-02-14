def by_seven_not_five(lower, upper):
    return [x for x in range(lower + 1, upper) if x % 7 == 0 and x % 5 != 0]

print(by_seven_not_five(int(input("Lower limit: ")), int(input("Upper limit: "))))