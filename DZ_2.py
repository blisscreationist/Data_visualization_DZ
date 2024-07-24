import numpy as np
import matplotlib.pyplot as plt


data_x = np.random.rand(5)
data_y = np.random.rand(5)

plt.scatter(data_x, data_y)

plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

plt.show()