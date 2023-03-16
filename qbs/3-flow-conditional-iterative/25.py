till = int(input("Create pattern till _ *s: "))

for i in range(1, till + 1):
    print((till - i) * "  ", "* " * (i), sep = "")