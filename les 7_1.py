"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        # дабы разобраться и плохо зная синтаксис сделаем по шагам
        b = str()
        for row in self.matrix:
            a = str()
            for i in list(row):
                a += str(i) + ' '
            b += str(a) + '\n'
        return b
        # return '\n'.join(' '.join([str(i) for i in row]) for row in self.matrix) можно было так

    def __add__(self, other):
        try:
            m = [[int(self.matrix[row][i]) + int(other.matrix[row][i]) for i in range(len(self.matrix[row]))]
                 for row in range(len(self.matrix))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 12, 1, 5], [2, 66, 4, 6], [-5, -1, 64, -8]]
m_2 = [['5', '7', '2', '3'], ['9', '2', '3', '-54'], ['1', '2', '3', '4']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print(mtrx_1, end='')
print('-' * 30)
print(mtrx_2, end='')
print('-' * 30)
print(f'Sum:\n{new_m}')
print('#' * 30)

m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['9', '-54'], ['12', '3', '16']]

print(Matrix(m_3))
print(Matrix(m_4))

print(Matrix(m_3) + Matrix(m_4))


