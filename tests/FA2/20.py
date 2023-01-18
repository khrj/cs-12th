print(",".join([str(num) for num in range(100, 401) if len(str_num := str(num)) == len([number for digit in str_num if (number := int(digit)) % 2 == 0])]))
