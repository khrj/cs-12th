integer = input("Enter integer: ")
if integer[-1:] == "4":
    print("Ends with 4")
elif integer[-1:] == "8":
    print("Ends with 8")
else:
    print("Ends with neither")