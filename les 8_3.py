'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_list_of_num():
    my_list = []
    while True:
        value = input('Введите значения и нажимайте Enter - ')
        if value == '':
            value = 'str'
        if value[0] == '.':
            value = 'str'
        try:
            for i in value:
                if ord(i) < 48 and ord(i) != 46 and ord(i) != 45 or value.count('.') >= 2 or ord(i) > 57 or i.count('.') > 2:
                    raise OwnError(f"Список должен состоятьтолко из чисел, введите любое действительное число")

        except OwnError as err:
            print(err)
            y = input(f'Попробовать еще раз? Введите Y для продолжения, любой другой символ - для выхода ')
            if y.upper == 'Y':
                    print(my_list_of_num())
            elif y.upper() != 'Y':
                return f'Вы вышли\n' \
                       f'Текущий список - {my_list} \n '

        else:
            my_list.append(value)
            print(f'Текущий список - {my_list} \n ')

print(my_list_of_num())

