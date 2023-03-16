dictionary = dict(
    [
        item.split("-")
        for item in input(
            "Enter dictionary (hyphen between key-value, comma between records): "
        ).split(",")
    ]
)

seen_values = []

for k, v in dictionary.copy().items():
    if v in seen_values:
        dictionary.pop(k)
    else:
        seen_values.append(v)

print(dictionary)