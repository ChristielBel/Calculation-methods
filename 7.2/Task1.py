import numpy as np
import time

# Реализация метода Симпсона
def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Ensure n is even
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)
    return result * h / 3

# Реализация метода Рунге-Кутты 4-го порядка для решения ОДУ
def rk4(dydx, x0, y0, x_end, num_steps):
    h = (x_end - x0) / num_steps
    x = x0
    y = y0

    for _ in range(num_steps):
        k1 = h * dydx(x, y)
        k2 = h * dydx(x + h / 2, y + k1 / 2)
        k3 = h * dydx(x + h / 2, y + k2 / 2)
        k4 = h * dydx(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

    return y

# Функция для численного решения задачи Коши через RK4
def erf_via_differential_equation(x_values):
    def dydx(x, y):
        return 2 / np.sqrt(np.pi) * np.exp(-x**2)

    results = []
    for x in x_values:
        result = rk4(dydx, 0, 0, x, 1000)  # 1000 steps for better accuracy
        results.append(result)
    return results

# Функция для расчета значений erf(x) через самописный метод Симпсона
def erf_via_simpson(x_values):
    def integrand(t):
        return 2 / np.sqrt(np.pi) * np.exp(-t**2)

    results = []
    for x in x_values:
        results.append(simpson_method(integrand, 0, x, 1000))
    return results

# Основная часть программы
if __name__ == "__main__":
    x_values = np.arange(0.0, 2.1, 0.1)

    # Решение через дифференциальное уравнение
    start_time = time.time()
    erf_diff_eq = erf_via_differential_equation(x_values)
    diff_eq_time = time.time() - start_time

    # Решение через самописный метод Симпсона
    start_time = time.time()
    erf_simpson = erf_via_simpson(x_values)
    simpson_time = time.time() - start_time

    # Вывод таблицы сравнения
    print("+------+---------------------+---------------------+")
    print("|  x   | Erf via Diff. Eq.   | Erf via Simpson     |")
    print("+------+---------------------+---------------------+")
    for x, diff_val, simp_val in zip(x_values, erf_diff_eq, erf_simpson):
        print(f"| {x:4.1f} | {diff_val:19.6f} | {simp_val:19.6f} |")
    print("+------+---------------------+---------------------+")

    # Вывод времени выполнения
    print(f"\nTime taken by Differential Equation method: {diff_eq_time:.6f} seconds")
    print(f"Time taken by Simpson method: {simpson_time:.6f} seconds")
