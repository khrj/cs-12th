matrix, row_len = [], None # stored as linear list

print("Enter a matrix, where each element is separated by a space. Press enter on an empty line to finish")
while ((elms := input().split(' ')) != ['']):
    if row_len and len(elms) != row_len: raise ValueError("row length mismatch")
    else: row_len = len(elms)
    matrix.extend(elms)

print([matrix[number_of_columns::row_len] for number_of_columns in range(row_len)])
