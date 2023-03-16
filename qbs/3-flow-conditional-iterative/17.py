a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")