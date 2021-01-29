#урок 3 Задача 4
def my_f(x, y):
    i = 1
    power = 1
    try:
        x, y = float(x), int(y)
        if 0 < x and 0 > y:
            while i <= abs(y):
                power = power / x
                i = i + 1
            print(f"{x} в степени ({y}): {round(power, 6)}")
        else:
            print('Введите положительное дейсвительное число и отрицательное целое')
    except ValueError:
        print('Программа работает только с числами')


my_f(2, '-8')