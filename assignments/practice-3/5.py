from itertools import product

values = dict(
    [
        [(spl := item.split("-"))[0], spl[1].split(",")]
        for item in input(
            "Enter dictionary (hyphen between key-value, comma between elms of value, semi-colon between records): "
        ).split(";")
    ]
).values()

print(["".join(x) for x in product(*values)])