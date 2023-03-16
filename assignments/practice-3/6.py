dicts = [
    dict([item.split("-") for item in dictionary.split(",")])
    for dictionary in input(
        "Enter list of dictionaries (hyphen between key-value, comma between records, semi-colon between dictionaries): "
    ).split(";")
]

summed = {}

for dictionary in dicts:
    if dictionary["item"] in summed:
        summed[dictionary["item"]] += int(dictionary["amount"])
    else:
        summed[dictionary["item"]] = int(dictionary["amount"])

print(summed)
