from random import randint
import numpy as np

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
COUNT = 4
ROWS = 8


def eight_queens(coordinates: list[list[int]]) -> bool:
    matrix = []
    for _ in range(ROWS):
        matrix.append([ZERO] * ROWS)

    for i in range(len(coordinates)):
        k = coordinates[i]
        for j in range(len(k) - ONE):
            h = k[j]
            v = k[j + ONE]
            matrix[h - ONE][v - ONE] = ONE
    # q =
    if np.sum(matrix) != ROWS:
        return False

    sum_str_list = np.sum(matrix, axis=ONE)
    for sum_str in sum_str_list:
        if sum_str > ONE:
            return False

    sum_rows_list = np.sum(matrix, axis=ZERO)
    for sum_rows in sum_rows_list:
        if sum_rows > ONE:
            return False

    for i in range(len(matrix)):
        a = np.trace(matrix, offset=i)
        b = np.trace(matrix, offset=-i)
        r = np.rot90(matrix)
        c = np.trace(r, offset=i)
        d = np.trace(r, offset=-i)
        if a | b | c | d > ONE:
            return False

    for i in range(ROWS):
        for j in range(ROWS):
            print(str(matrix[i][j]).rjust(THREE), end=' ')
        print()

    return True


def random_coordinates() -> list[list[int]]:
    return [[randint(1, 8) for _ in range(TWO)] for _ in range(ROWS)]


if __name__ == '__main__':
    coord = random_coordinates()
    print(eight_queens(coord))

    # очень долго работает:

    # while COUNT:
    #     coord = random_coordinates()
    #     if eight_queens(coord):
    #         print(coord)
    #         print()
    #         COUNT -= ONE
