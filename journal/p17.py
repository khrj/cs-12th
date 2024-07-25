stk = []

while True:
    name = input("Enter book name (EOF to end): ")
    if name == "EOF":
        break
    pages = int(input("Number of pages: "))
    price = int(input("Price: "))

    if pages < 200:
        stk.append((name, pages, price))

while len(stk) > 0:
    book = stk.pop()
    print(book)