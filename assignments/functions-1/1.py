def my_max(one, two, three):
    return max((one, two, three))


print(
    my_max(
        float(input("Enter first: ")),
        float(input("Enter second: ")),
        float(input("Enter third: ")),
    )
)
