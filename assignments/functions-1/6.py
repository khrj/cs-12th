def n_pascal(n):
    pad = n - 1

    parent_row = []

    for row_num in range(0, n):
        actual_pad = pad - row_num
        print(" " * actual_pad, end="")

        row = [1]

        for i in range(len(parent_row)):
            if i + 1 >= len(parent_row):
                row.append(1)
            else:
                pair_sum = parent_row[i] + parent_row[i + 1]
                row.append(pair_sum)

        parent_row = row
        print(" ".join([str(x) for x in row]))


n_pascal(int(input("Enter number of rows: ")))
