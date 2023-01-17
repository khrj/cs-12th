from math import floor, sqrt

sqrt_of_number = sqrt(float(input("Enter a number: ")))

if (sqrt_of_number == 1 or sqrt_of_number == 0):
    print("Square root of number is neither prime nor composite")
    exit()

for i in range(2, floor(sqrt(sqrt_of_number))):
    if sqrt_of_number % i == 0:
        print("Square root of number is not prime")
        exit()

print("Square root of number is prime")