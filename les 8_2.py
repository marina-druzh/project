'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


divident, divider = input('Введите делимое и делитель: ').split()
try:
    dvt, dvr = map(float, (divident, divider))
    if dvr == 0:
        raise OwnError("Операция невозможна! Делить на ноль нельзя!")
except ValueError:
    print("Делимое и делитель должны быть числами")
except OwnError as err:
    print(err)
else:
    print("Результат:", round(dvt / dvr, 5))
