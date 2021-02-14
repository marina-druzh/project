'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''

class ComplexNum:
    def __init__(self, a, b, ind='Комплексное число'):
        self.a = a
        self.b = b
        self.z = f'{self.a} + {self.b}j'
        self.ind = ind

    def __add__(self, other):
        z_ind = 'Сложение комплексных чисел: '
        z_a = self.a + other.a
        z_b = self.b + other.b
        return ComplexNum(z_a, z_b, z_ind)

    def __mul__(self, other):
        z_ind = 'Произведение комплексных чисел: '
        z_a = self.a * other.a - (self.b * other.b)
        z_b = self.a * other.b + other.a * self.b
        return ComplexNum(z_a, z_b, z_ind)

    def __str__(self):
        return f'{self.ind} z = {self.a} + {self.b}j'


z_1 = ComplexNum(1, -2)
z_2 = ComplexNum(3, 4)
z_3 = ComplexNum(-5, 2)

print(z_1)

print(z_1 + z_2)
print(z_1 + z_2 + z_3)
print(z_1 * z_2 * z_3)
print(z_1 * z_2, '\n')


#Проверка правильности работы программы

r = complex(1, -2)
t = complex(3, 4)
y = complex(-5, 2)
print('Multiplication: ', r * t * y)
print('Summ: ', r + t + y)