from datetime import date


def isLeapYear():
    yr = date.today().year
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)


data = {
    "january": 31,
    "february": 29 if isLeapYear() else 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31,
}

print(data[input("Enter month: ").lower()], "days")
print(sorted(data.keys()))
print([m for m, d in data.items() if d == 31])
print([[k, v] for k, v in sorted([[v, k] for k, v in data.items()])])
