import numpy as np
import matplotlib.pyplot as plt

# Определим функцию f(x)
def f(x):
    return 1 / (1 + 25 * x**2)


def cubic_spline(nodes, values, x_vals):
    n = len(nodes) - 1  # Количество интервалов

    # Вычисляем шаги между узлами
    h = np.diff(nodes)

    # Вычисляем правую часть уравнений для сплайна
    alpha = np.zeros(n + 1)
    for i in range(1, n):
        alpha[i] = (3 / h[i] * (values[i + 1] - values[i]) - 3 / h[i - 1] * (values[i] - values[i - 1]))

    # Решаем систему уравнений для c
    l = np.ones(n + 1)
    mu = np.zeros(n + 1)
    z = np.zeros(n + 1)

    for i in range(1, n):
        l[i] = 2 * (nodes[i + 1] - nodes[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    c = np.zeros(n + 1)
    b = np.zeros(n)
    d = np.zeros(n)
    a = values[:-1]

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (values[j + 1] - values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Вычисляем сплайн для всех значений x_vals
    spline_values = np.zeros_like(x_vals)
    for i in range(n):
        mask = (x_vals >= nodes[i]) & (x_vals <= nodes[i + 1])
        dx = x_vals[mask] - nodes[i]
        spline_values[mask] = a[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    return spline_values

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
    spline_interp = cubic_spline(nodes, values, x_vals)
    
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
