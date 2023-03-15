def count_digit_char(string):
    return len([x for x in string if x.isalpha()]), len([x for x in string if x.isdigit()])


print(count_digit_char(input("Enter string: ")))
