""" Exercise 1
        Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
        который должен принимать данные (список списков) для формирования матрицы.

        Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
        Примеры матриц вы найдете в методичке.

        Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
        Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
        Matrix (двух матриц). Результатом сложения должна быть новая матрица.

        Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
        складываем с первым элементом первой строки второй матрицы и т.д.
"""
# from typing import List


class Matrix:

    def __init__(self, matrix_in: list):
        self.matrix = matrix_in

    def __add__(self, other):
        len_1 = len(self.matrix)
        len_2 = len(self.matrix[0])
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len_2)] for i in range(len_1)])

    def __str__(self):
        return "Запрошенная матрица:\n" + '\n'.join(['\t'.join([str(el) for el in line]) for line in self.matrix])


# Define variables(matrix)
matrix_3x2_1 = [[1, 2],
                [10, 1],
                [-5, 3]]
matrix_3x2_2 = [[5, 10],
                [3, 0],
                [-1, 2]]
matrix_3x3_1 = [[-1, 2, 6],
                [7, -3, 5],
                [9, -1, 2]]
matrix_3x3_2 = [[8, -3, 0],
                [-2, 4, -8],
                [2, -2, 3]]
matrix_2x4_1 = [[10, -4, 0, -1],
                [-1, 5, -1, -9]]
matrix_2x4_2 = [[2, 7, 3, 4],
                [-4, 6, 2, 10]]

matrix_1 = Matrix(matrix_3x2_1)
matrix_2 = Matrix(matrix_3x2_2)
matrix_3x2_result = matrix_1 + matrix_2
print(matrix_3x2_result.__str__())

matrix_1 = Matrix(matrix_3x3_1)
matrix_2 = Matrix(matrix_3x3_2)
matrix_3x3_result = matrix_1 + matrix_2
print(matrix_3x3_result.__str__())

matrix_1 = Matrix(matrix_2x4_1)
matrix_2 = Matrix(matrix_2x4_2)
matrix_2x4_result = matrix_1 + matrix_2
print(matrix_2x4_result.__str__())
