# probably not the solution they want
from math import factorial
print(factorial(int(input("Enter a number: "))))

# likely what was wanted
number = int(input("Enter a number: "))
product = 1

for i in range(2, number + 1):
    product *= i

print(product)