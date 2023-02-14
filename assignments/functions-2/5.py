from math import prod


def mdr_and_mpers(num_str, depth=0):
    if len(num_str) > 1:
        return mdr_and_mpers(str(prod([int(x) for x in num_str])), depth + 1)
    else:
        return (num_str, depth)


print(mdr_and_mpers(input("Enter number: ")))
