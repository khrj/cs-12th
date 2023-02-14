def calc_upper_lower(string):
    return len([x for x in string if x.isupper()]), len([x for x in string if x.islower()])

print(calc_upper_lower(input("Enter string: ")))
