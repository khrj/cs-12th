till = int(input("Create pattern till _ numbers: "))

for i in range(1, till + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()