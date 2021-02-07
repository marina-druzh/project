'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу
декоратора @property.
'''

from abc import ABC, abstractmethod


# class MyAbstractClass(ABC):
#     @abstractmethod
#     def consumption(self):
#         pass


class Clothes(ABC):
    result = 0

    def __str__(self):
        return f"Общее количество ткани: {Clothes.result}"

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Clothes.result

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5)
        # result = round(self.size / 6.5 + 0.5, 2)
        # Clothes.consumption_Coat = result
        # return f'Расход ткани для пальто {self.size} размера = {round(self.size / 6.5 + 0.5, 2)} м ткани'


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return round((2 * self.height + 0.3) / 100)
        # result = round(2 * self.height + 0.3, 2)
        # Clothes.consumption_Costume = result
        # return f'Расход ткани для костюма на рост {self.height} = {round((2 * self.height + 0.3) / 100, 2) } м ткани'



my_2 = Coat(44)
my_3 = Costume(183)
my_4 = Costume(168)

print(f'Расход ткани для пальто размера {my_2.size} - {my_2.consumption} м')
print(f'Расход ткани для костюма на рост {my_3.height} - {my_3.consumption} м')
print(my_2 + my_3)
print(Clothes.result)
print(Clothes.consumption)
