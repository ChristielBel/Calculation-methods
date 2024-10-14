import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Определим функцию f(x)
def f(x):
    return 1 / (1 + 25 * x**2)

# Узлы Чебышёва
def chebyshev_nodes(n):
    return np.cos((2*np.arange(1, n+1) - 1) / (2*n) * np.pi)

# Интерполяция Лагранжа
def lagrange_interpolation(x, nodes, values):
    poly = lagrange(nodes, values)
    return poly(x)

# Параметры
x_vals = np.linspace(-1, 1, 500)  # Точки для построения графика
n_values = [5, 10, 15]  # Значения n для интерполяции

# Построение графика
plt.figure(figsize=(14, 10))

for i, n in enumerate(n_values):
    # Равноотстоящие узлы
    equal_nodes = np.linspace(-1, 1, n)
    equal_values = f(equal_nodes)
    
    # Узлы Чебышёва
    cheb_nodes = chebyshev_nodes(n)
    cheb_values = f(cheb_nodes)
    
    # Построение интерполяционных полиномов
    equal_interp = lagrange_interpolation(x_vals, equal_nodes, equal_values)
    cheb_interp = lagrange_interpolation(x_vals, cheb_nodes, cheb_values)
    
    # Оригинальная функция
    plt.subplot(2, len(n_values), i+1)
    plt.plot(x_vals, f(x_vals), 'b-', label='f(x)')
    plt.plot(x_vals, equal_interp, 'r--', label=f'Равноотстоящие узлы (n={n})')
    plt.scatter(equal_nodes, equal_values, color='red')
    plt.title(f"Равноотстоящие узлы, n={n}")
    plt.legend()
    
    # Интерполяция с узлами Чебышёва
    plt.subplot(2, len(n_values), i+1+len(n_values))
    plt.plot(x_vals, f(x_vals), 'b-', label='f(x)')
    plt.plot(x_vals, cheb_interp, 'g--', label=f'Узлы Чебышёва (n={n})')
    plt.scatter(cheb_nodes, cheb_values, color='green')
    plt.title(f"Узлы Чебышёва, n={n}")
    plt.legend()

plt.tight_layout()
plt.show()
