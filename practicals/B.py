from csv import reader, writer


def add():
    cellid = int(input("Enter cell id: "))
    brandname = input("Enter brand name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price: "))

    with open("cellphone.csv", "a", newline="") as f:
        w = writer(f)
        w.writerow([cellid, brandname, quantity, price])


def display():
    with open("cellphone.csv", "r", newline="") as f:
        r = reader(f)
        next(r) # skip header
        for row in r:
            print(f"Cell ID: {row[0]}")
            print(f"Brand name: {row[1]}")
            print(f"Quantity: {row[2]}")
            print(f"Price: {row[3]}")
            print()


def search():
    with open("cellphone.csv", "r", newline="") as f:
        search = input("Enter cell ID to search for: ")
        r = reader(f)
        next(r) # skip header
        found = False

        for row in r:
            if row[0] == search:
                print("Record found: ")
                print(f"Cell ID: {row[0]}")
                print(f"Brand name: {row[1]}")
                print(f"Quantity: {row[2]}")
                print(f"Price: {row[3]}")
                found = True

        if not found:
            print("No record found")


# make sure there's a header
with open("cellphone.csv", "a+", newline="") as f:
    f.seek(0)
    lines = len(f.readlines())
    if lines <= 1:
        f.seek(0)
        w = writer(f)
        w.writerow(["cellid", "brandname", "quantity", "price"])


while True:
    print("What would you like to do?")
    print("1. Add record")
    print("2. Display records")
    print("3. Search records by Cell ID")
    print("4. Exit")

    choice = input("Enter choice: ")
    print()

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

    print()
