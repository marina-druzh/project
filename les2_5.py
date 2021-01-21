'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
'''
'''
my_list = [8, 7, 7, 7, 5, 4, 3, 2, 2]
rank = int(input('Введите натуральное число  '))
if rank < 0:
    rank = int(input('Число должно быть больше нуля!\nВведите число снова  '))
for i, el in enumerate(my_list, start=1):
    if el == rank:
        q = my_list.count(el)
        my_list.insert(i + q - 1, el)
        print(my_list)
        break
'''
my_list = [8, 7, 7, 7, 5, 4, 3, 2, 2]
my_l = list(my_list)
rank = int(input('Введите натуральное число  '))
if rank < 0:
    rank = int(input('Число должно быть больше нуля!\nВведите число снова  '))
for i, el in enumerate(my_list, start=1):
    if rank < my_list[len(my_list)-1]:
        my_list.insert(len(my_list) + 1, rank)
        print(f"{my_l}\n{my_list}")
        break
    if rank > el:
        my_list.insert(i-1, rank)
        print(f"{my_l}\n{my_list}")
        break
    if el == rank:
        q = my_list.count(el)
        my_list.insert(i + q - 1, el)
        print(f"{my_l}\n{my_list}")
        break
