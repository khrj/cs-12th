a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))

if a + b > c and a + c > b and b + c > a:
    print(f"A triangle can be formed with sides of length {a}, {b} and {c}")
else:
    print(f"A triangle cannot be formed with sides of length {a}, {b} and {c}")