def factorial(number):
    if number == 1 or number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(int(input("Enter number: "))))
