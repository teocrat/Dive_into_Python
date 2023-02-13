ZERO = 0


def trans_matrix(matrix: list[list]) -> list[list]:
    matrix_trans = [[ZERO for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_trans[j][i] = matrix[i][j]
    return matrix_trans


matrix = [[1, 2, 3], [4, 5, 6]]
res = trans_matrix(matrix)
print(matrix)
print(res)
