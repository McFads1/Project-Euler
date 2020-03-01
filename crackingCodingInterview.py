# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O

def zeroColumn(matrix, col_index):
    for item in matrix:
        item[col_index] = 0
    return matrix

def zeroRow(matrix, row_index):
    for index, item in enumerate(matrix[row_index]):
        matrix[row_index][index] = 0
    return matrix

def zeroMatrix():
    rows_to_zero = []
    cols_to_zero = []
    matrix = [
        [1, 2, 3, 4, 0],
        [1, 2, 0, 3, 4],
        [2, 3, 5, 2, 1],
        [4, 3, 2, 1, 5]
    ]
    for row_index, row in enumerate(matrix):
        for col_index, item in enumerate(row):
            if item == 0:
                rows_to_zero.append(row_index)
                cols_to_zero.append(col_index)

    rows_to_zero = list(set(rows_to_zero))
    cols_to_zero = list(set(cols_to_zero))

    for row in rows_to_zero:
        matrix = zeroRow(matrix, row)
    for col in cols_to_zero:
        matrix = zeroColumn(matrix, col)
    return matrix
