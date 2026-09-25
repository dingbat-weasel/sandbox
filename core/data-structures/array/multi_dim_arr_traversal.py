input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def row_major_traversal(matrix: list[list[int]]) -> list[int]:
    """
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    # double for loop - unnecessary inner loop
    # out = []
    # for row in matrix:
    #     for val in row:
    #         out.append(val)
    # return out

    # extend the list by adding all items at once
    out = []
    for row in matrix:
        out.extend(row)
    return out

    # list comprehension
    # return [val for row in matrix for val in row]


print(row_major_traversal(input))


def col_major_traversal(matrix: list[list[int]]) -> list[int]:
    """
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Output: [1, 4, 7, 2, 5, 8, 3, 6, 9]
    """
    out = []
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return out

    row_len = len(matrix[0])
    for i in range(row_len):
        for row in matrix:
            out.append(row[i])
    return out


print(col_major_traversal(input))
