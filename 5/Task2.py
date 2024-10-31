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
    n = len(nodes)  # Количество узлов
    result = np.zeros_like(x, dtype=float)  # Массив для хранения результатов интерполяции

    # Вычисляем полином Лагранжа для каждого значения x
    for i in range(n):
        # Начинаем с базисного полинома l_i(x), который изначально равен 1
        li = np.ones_like(x, dtype=float)

        # Строим l_i(x)
        for j in range(n):
            if i != j:
                li *= (x - nodes[j]) / (nodes[i] - nodes[j])

        # Добавляем вклад y_i * l_i(x) в общий результат
        result += values[i] * li

    return result

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
    
    # Интерполяционные полиномы
    equal_interp = lagrange_interpolation(x_vals, equal_nodes, equal_values)
    cheb_interp = lagrange_interpolation(x_vals, cheb_nodes, cheb_values)
    
    # Отклонение от исходной функции
    equal_error = np.abs(f(x_vals) - equal_interp)
    cheb_error = np.abs(f(x_vals) - cheb_interp)
    
    # График отклонений для равноотстоящих узлов
    plt.subplot(2, len(n_values), i+1)
    plt.plot(x_vals, equal_error, 'r-', label=f'Отклонение для равноотстоящих узлов (n={n})')
    plt.title(f"Равноотстоящие узлы, n={n}")
    plt.legend()
    
    # График отклонений для узлов Чебышёва
    plt.subplot(2, len(n_values), i+1+len(n_values))
    plt.plot(x_vals, cheb_error, 'g-', label=f'Отклонение для узлов Чебышёва (n={n})')
    plt.title(f"Узлы Чебышёва, n={n}")
    plt.legend()

plt.tight_layout()
plt.show()
