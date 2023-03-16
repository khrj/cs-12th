(items := input("Enter items separated by commas: ").split(',')) and (indices := input("Enter indices separated by commas: ").split(",")) and print([items[int(x)] for x in indices])
