# SAME AS p01

from math import pi

while True:
    print("Enter a solid figure to calculate the area for:")
    print("1. Sphere")
    print("2. Cuboid")
    print("3. Cone")
    print("4. Cylinder")
    figure = int(input("Enter selection: "))

    if figure == 1:
        r = int(input("Enter r: "))
        print("Surface area of sphere:", 4 * pi * r**2)
        print("Volume of sphere:", 4 / 3 * pi * r**3)
    elif figure == 2:
        l, b, h = int(input("Enter l: ")), int(input("Enter b: ")), int(input("Enter h: "))
        print("Surface area of cuboid:", (l * b + b * h + l * h) * 2)
        print("Volume of cuboid:", l * b * h)
    elif figure == 3:
        r, h = int(input("Enter r: ")), int(input("Enter h: "))
        l = (r**2 + h**2) ** (1 / 2)
        print("Surface area of cone:", pi * r * l)
        print("Volume of cone:", 1 / 3 * pi * r**2 * h)
    elif figure == 4:
        r, h = int(input("Enter r: ")), int(input("Enter h: "))
        print("Surface area of cylinder:", 2 * pi * r**2 + 2 * pi * r * h)
        print("Volume of cylinder:", pi * r**2 * h)
