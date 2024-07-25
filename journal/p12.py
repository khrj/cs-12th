def copyFile(fromFile, toFile):
    readable = open(fromFile, "r")
    writeable = open(toFile, "w")

    lines = readable.readlines()
    lines[0] = lines[0].upper()
    lines[1] = lines[1].lower()

    writeable.writelines(lines)
    
copyFile(
    input("Enter from file: "),
    input("Enter to file: ")
)
