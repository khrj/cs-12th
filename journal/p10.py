def copyAM(fromFile, toFile):
    readable = open(fromFile, "r")
    writeable = open(toFile, "w")

    lines = readable.readlines()

    for line in lines:
        if line.startswith("a") or line.startswith("m"):
            writeable.write(line)

    writeable.flush()

copyAM(
    input("Enter from file: "),
    input("Enter to file: ")
)
