import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Определим функцию f(x)
def f(x):
    return 1 / (1 + 25 * x**2)

# Параметры
x_vals = np.linspace(-1, 1, 500)  # Точки для построения графика
n_values = [5, 10, 15]  # Значения n для интерполяции

# Построение графика
plt.figure(figsize=(14, 10))

for i, n in enumerate(n_values):
    # Узлы интерполяции
    nodes = np.linspace(-1, 1, n)
    values = f(nodes)
    
    # Кубическая интерполяция сплайнами
    cubic_spline = CubicSpline(nodes, values)
    spline_interp = cubic_spline(x_vals)
    
    # Оригинальная функция
    plt.subplot(2, len(n_values), i+1)
    plt.plot(x_vals, f(x_vals), 'b-', label='f(x)')
    plt.plot(x_vals, spline_interp, 'r--', label=f'Кубический сплайн (n={n})')
    plt.scatter(nodes, values, color='red')
    plt.title(f"Кубический сплайн, n={n}")
    plt.legend()
    
    # Отклонение от исходной функции
    spline_error = np.abs(f(x_vals) - spline_interp)
    
    # График отклонений
    plt.subplot(2, len(n_values), i+1+len(n_values))
    plt.plot(x_vals, spline_error, 'g-', label=f'Отклонение сплайна (n={n})')
    plt.title(f"Отклонение сплайна, n={n}")
    plt.legend()

plt.tight_layout()
plt.show()
