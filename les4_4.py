"""
Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке. Для выполнения задания
обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

from random import randint

my_list = [randint(-10, 101) for i in range(20)]
print(my_list)


def get_unique(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


print(get_unique(my_list))
