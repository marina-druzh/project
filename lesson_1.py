import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(2*x))
plt.title('Косинусоида', fontsize=17)
plt.axis()
plt.legend(['cos(x)', 'cos(2x)'])
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

