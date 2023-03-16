till = int(input("Create pattern till _ *s: "))

# much nicer to use string replication but they want nested for loop

# for i in range(0, till):
#     for j in range(1, i + 1):
#         print("*", end=" ")
    
#     print()


# for i in range(till, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")

#     print()

for i in range(1, till):
    print("* " * i)

for i in range(till, 0, -1):
    print("* " * i)

    