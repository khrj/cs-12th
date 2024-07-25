from pickle import dump
opened = open("Electronics.dat", "wb")

store = []

def takeInput(itemCount):
    print("Enter", itemCount, "item names, company names, quantities, prices separated by commas: ")
    for i in range(itemCount):
        itemname, companyname, quantity, price = input().split(",")
        quantity = int(quantity)
        price = int(price)
        store.append([itemname, companyname, quantity, price])

takeInput(10)
dump(store, opened)
takeInput(2)
opened.seek(0)
dump(store, opened)

print("TVs")
for record in store:
    if record[0].lower() == "tv":
        print(record)

total = 0
for record in store:
    total += record[3] * record[2]

print("Total investment:", total)

print("Samsung-branded items")
for record in store:
   if record[1].lower() == "samsung":
       print(record[0])

for record in store:
   if record[1].lower() == "lg" and record[0].lower() == "washing machine":
       record[3] = record[3] + 100
