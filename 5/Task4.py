import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Данные из таблицы
x = np.array([2, 3, 5, 7])
f_x = np.array([4, -2, 6, -3])

# Построение кубического сплайна
cs = CubicSpline(x, f_x)

# Проверка значений сплайна в узловых точках
spline_values_at_nodes = cs(x)

# Вывод значений сплайна в узловых точках для проверки
print("Значения сплайна в узловых точках:")
for i in range(len(x)):
    print(f"S({x[i]}) = {spline_values_at_nodes[i]}, f({x[i]}) = {f_x[i]}")

# Построение графика
x_vals = np.linspace(min(x), max(x), 500)  # Для плавного графика
spline_vals = cs(x_vals)

# Построение графика кубического сплайна и узловых точек
plt.figure(figsize=(8, 6))
plt.plot(x_vals, spline_vals, label='Кубический сплайн', color='blue')
plt.scatter(x, f_x, color='red', label='Узловые точки')
plt.title("Кубический сплайн для заданных точек")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
