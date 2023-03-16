num_map = dict(zip([str(x) for x in range(1,11)], ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")))
print(" ".join([num_map[char] for char in input("Enter number: ")]))