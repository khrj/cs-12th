mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}

digit = input("Enter a digit: ")

try:
    print(f"{digit} in words is {mapping[digit]}")
except KeyError:
    print("Invalid input")