def lessThan4Letters(fromFile):
    readable = open(fromFile, "r")
    
    words = readable.read().replace("\n", " ").split(" ")
    for word in words:
        if len(word) < 4:
            print(word)
    
lessThan4Letters(input("Enter file: "))
