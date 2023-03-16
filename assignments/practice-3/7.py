dictionary = dict(
    [
        [(spl := item.split("-"))[0], spl[1].split(",")]
        for item in input(
            "Enter dictionary (hyphen between key-value, comma between elms of value, semi-colon between records): "
        ).split(";")
    ]
)

list_of_dictionaries = []
keys = list(dictionary.keys())

for i in range(0, len(dictionary[keys[0]])):
    this_dictionary = {}

    for key in keys:
        this_dictionary[key] = dictionary[key][i]
    
    list_of_dictionaries.append(this_dictionary)

print(list_of_dictionaries)
