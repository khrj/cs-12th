(lim := int(input("Till: "))) and print("\n".join(["* " * row_limit for row_limit in [*range(1, lim), *range(lim, 0, -1)]]))
