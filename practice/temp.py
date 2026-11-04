def col(mat: list[list[int]]) -> list:
    out = []
    if len(mat) == 0 or len(mat[0]) == 0:
        return out

    for i in range(len(mat[0])):
        for row in mat:
            out.append(row[i])

    return out


print(col([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
