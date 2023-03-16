print((sqrt := int(int(input("Enter number: ")) ** 0.5)) and len([x for x in range(2, sqrt) if sqrt % x == 0]) == 0)
