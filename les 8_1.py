'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
'''


class Data:
    date = 0
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        try:

            my_date = str(day_month_year).split('-')
            date = [(int(my_date[i])) for i in range(len(my_date))]
            day, month, year = map(int, date)
            return day, month, year
        except ValueError:
            return 'Дата введена неверно'

    @staticmethod
    def check(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2099 >= year >= 0:
                    valid_date = '.'.join(map(str, [day, month, year]))
                    return f'Дата введена верно: {valid_date}'
                else:
                    return f'Неверно задан год'
            else:
                return f'Неверно задан месяц'
        else:
            return f'Неверно задан день'

    def __str__(self):
        return f'Введена дата {self.day_month_year}'



today = Data.extract('11 - 13 -2001')
today1 = Data.extract('11  13 -2001')
print(today)
print(today1)
print(Data.check(11, 11, 2022))
print(Data.check(11, 13, 2022))
print(Data.check(45, 12, 2022))
print(Data.check(11, 11, 68682))
