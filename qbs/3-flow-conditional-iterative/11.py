items = int(input("Enter number of items: "))
if items < 10:
    print(f"Cost: ₹{items * 120}")
elif 10 <= items <= 99:
    print(f"Cost: ₹{items * 100}")
else:
    print(f"Cost: ₹{items * 70}")