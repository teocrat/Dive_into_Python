from random import randint

import numpy

ZERO = 0
MIN_RANDOM = 0
MAX_RANDOM = 100
FOUR = 4


class Matrix:
    """Класс для создания  матриц, сложения матриц и сравнения. Принимает аргументы:
    количество рядов и столбцов"""

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

    def build_matrix(self):
        """Метод для построения матрицы со случайными числами"""

        for _ in range(self.rows):
            col = []
            for _ in range(self.columns):
                col.append(randint(MIN_RANDOM, MAX_RANDOM))
            self.matrix.append(col)
        return self.matrix

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            return 'Матрицы разных размеров. Сложение невозможно'
        self.matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[ZERO]))]
                       for i in range(len(self.matrix))]
        return self

    def __eq__(self, other):
        return numpy.array_equal(self.matrix, other.matrix)

    def __str__(self):
        s = ''
        for i in range(self.rows):
            for j in range(self.columns):
                s += str(self.matrix[i][j]).rjust(FOUR)
            s += '\n'
        return s


if __name__ == '__main__':
    m1 = Matrix(3, 4)
    m1.build_matrix()
    print(m1)
    m2 = Matrix(3, 4)
    m2.build_matrix()
    print(m2)
    print(m1 == m2)
    print()
    m3 = m1 + m2
    print(m3)
    

