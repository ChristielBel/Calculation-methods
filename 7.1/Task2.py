import math
import numpy as np


# Функция для вычисления кубического сплайна
def cubic_spline(x, y):
    n = len(x) - 1
    h = np.diff(x)

    # Матрица коэффициентов A и правая часть B для системы уравнений
    A = np.zeros((n + 1, n + 1))
    B = np.zeros(n + 1)

    # Заполнение матрицы A и вектора B
    A[0, 0] = 1  # Граничное условие: натуральный сплайн
    A[n, n] = 1  # Граничное условие: натуральный сплайн
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        B[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    # Решение системы для получения коэффициентов c
    c = np.linalg.solve(A, B)

    # Вычисление коэффициентов b и d
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    # Функция для вычисления значения сплайна в точке xi
    def spline_func(xi):
        for i in range(n):
            if x[i] <= xi <= x[i + 1]:
                dx = xi - x[i]
                return y[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
        return None

    return spline_func

# Подынтегральная функция
def f(x):
    return 4 / (1 + x ** 2)


# Метод левых прямоугольников
def left_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n))
    return result * h


# Метод правых прямоугольников
def right_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + (i + 1) * h) for i in range(n))
    return result * h


# Метод центральных прямоугольников
def midpoint_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + (i + 0.5) * h) for i in range(n))
    return result * h


# Метод трапеций
def trapezoidal_method(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n))
    return result * h


# Сплайн-квадратуры ошибка здесь будет пропорциональна примерно h^4
def spline_quadrature(a, b, n):
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    spline_func = cubic_spline(x_values, y_values)

    # Интегрируем кубический сплайн с помощью численного метода (метода трапеций)
    integral = 0.0
    for i in range(n):
        integral += (x_values[i + 1] - x_values[i]) * (spline_func(x_values[i]) + spline_func(x_values[i + 1])) / 2
    return integral

def approximate_pi():
    actual_pi = math.pi
    n_values = [8, 32, 128]

    print(
        " n  | Left Rect      | Right Rect     | Mid Rect       | Trapezoidal   | Spline        | Actual π       | Left Rect Err | Right Rect Err | Mid Rect Err  | Trapezoidal Err | Spline Err  ")
    print(
        "----|----------------|----------------|----------------|---------------|---------------|----------------|---------------|----------------|---------------|-----------------|-------------")
    for n in n_values:
        h = 1 / n
        left_rect = left_rectangle_method(0, 1, n)
        right_rect = right_rectangle_method(0, 1, n)
        mid_rect = midpoint_rectangle_method(0, 1, n)
        trap_result = trapezoidal_method(0, 1, n)
        spline_result = spline_quadrature(0, 1, n)

        left_rect_error = abs(left_rect - actual_pi)
        right_rect_error = abs(right_rect - actual_pi)
        mid_rect_error = abs(mid_rect - actual_pi)
        trap_error = abs(trap_result - actual_pi)
        spline_error = abs(spline_result - actual_pi)

        print(
            f"{n:3d} | {left_rect:14.10f} | {right_rect:14.10f} | {mid_rect:14.10f} | {trap_result:13.10f} | {spline_result:13.10f} | {actual_pi:14.10f} | {left_rect_error:13.10f} | {right_rect_error:14.10f} | {mid_rect_error:13.10f} | {trap_error:15.10f} | {spline_error:11.10f}")

approximate_pi()
