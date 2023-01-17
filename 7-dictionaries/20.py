from datetime import date

def isLeapYear():
    yr = date.today().year
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)

data = {
    "february": 29 if isLeapYear() else 28,
    **dict.fromkeys(("january", "march", "may", "july", "august", "october", "december"), 31),
    **dict.fromkeys(("april", "june", "september", "november"), 30)
}

print(data[input("Enter month: ").lower()], "days")
print(sorted(data.keys()))
print([m for m, d in data.items() if d == 31])
print([[k, v] for k, v in sorted([[v, k] for k, v in data.items()])])
