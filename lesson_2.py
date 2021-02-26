import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 11, 50)
y1 = [-17/8*i**2 + 25/2 * i - 67/8 for i in x1]


# Построение графика
plt.title('Парабола: y = -17/8*x^2 +25/2*x - 67/8')
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.grid() # включение отображение сетки
plt.plot(x1, y1)

#проверка - построение точек на графике
x = [1, 3, 5]
y = [-17 / 8 * i ** 2 + 25 / 2 * i - 67 / 8 for i in x]
print(x, y)
plt.scatter(x, y, color='orange', s=40, marker='o')
plt.show()
