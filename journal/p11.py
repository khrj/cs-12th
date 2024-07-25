def countFromFile(fileName):
    readable = open(fileName, "r")
    content = readable.read()
    print(content.lower().count("india"))

countFromFile(input("Enter filename: "))
