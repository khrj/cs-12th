from pickle import load, dump


def add():
    shoeid = int(input("Enter shoe id: "))
    brandname = input("Enter brand name: ")
    size = int(input("Enter size: "))
    price = int(input("Enter price: "))

    with open("shoes.dat", "ab") as f:
        dump([shoeid, brandname, size, price], f)


def display():
    with open("shoes.dat", "rb") as f:
        try:
            while True:
                data = load(f)
                print(f"Shoe ID: {data[0]}")
                print(f"Brand name: {data[1]}")
                print(f"Size: {data[2]}")
                print(f"Price: {data[3]}")
                print()
        except EOFError:
            pass


def search():
    with open("shoes.dat", "rb") as f:
        search = int(input("Enter shoe ID to search for: "))
        found = False

        try:
            while True:
                data = load(f)
                if data[0] == search:
                    print("Record found: ")
                    print(f"Shoe ID: {data[0]}")
                    print(f"Brand name: {data[1]}")
                    print(f"Size: {data[2]}")
                    print(f"Price: {data[3]}")
                    print()

                    found = True
        except EOFError:
            pass

        if not found:
            print("No record found")


while True:
    print("What would you like to do?")
    print("1. Add record")
    print("2. Display records")
    print("3. Search records by Shoe ID")
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
