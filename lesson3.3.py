import numpy as np
import matplotlib.pyplot as plt
import math

# """задание 3.1 - Перевод полярных координат в декартовы"""
def polar_to_dec(phi, r):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    plt.plot(0, 0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.scatter(x, y, color='orange', s=40, marker='o')
    plt.grid(True)
    plt.show()


try:
    phi = float(input('Введите полярный угол точки: '))
    r = float(input('Введите полярный радиус точки: '))
    polar_to_dec(phi, r)
except ValueError:
    print('Вводимые данные должны быть числами!')



"""задание 3.3 - Посторение графика отрезка прямой линии в полярных координатах"""
def polar_plot():
    print('Посторение графика отрезка прямой линии в полярных координатах')
    k = float(input('Введите угловой коэффициент прямой: '))
    b = float(input('Введите смещение прямой по оси Y: '))
    x_1 = float(input('Введине координату х точки А: '))
    x_2 = float(input('Введине координату х точки B: '))
    x = (x_1, x_2)
    k = float(input('Введите угловой коэффициент прямой: '))
    b = float(input('Введите смещение прямой по оси Y: '))
    y = [k * i + b for i in x]
    #арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).
    phi = [math.atan2(y[i], x[i]) for i in range(len(x))]
    r = [math.sqrt(x[i]**2 + y[i]**2) for i in range(len(x))]
    for i in range(len(x)):
        plt.polar(phi, r)
    plt.grid(True)
    plt.show()


try:
    polar_plot()
except ValueError:
    print('Вводимые данные должны быть числами!')
