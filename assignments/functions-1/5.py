def is_perfect(number):
    return sum([divisor for divisor in range(1, number) if number % divisor == 0]) == number

print(is_perfect(int(input("Enter number: "))))