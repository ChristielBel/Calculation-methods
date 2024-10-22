import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
x = np.array([2, 6, 10, 14, 18, 22])
y = np.array([3.1, 6.7, 9.5, 11.9, 14.0, 15.5])


# x = np.array([1,2,3,4,5,6])
# y=np.array([1,1.5,3.0,4.5,7.0,8.5])
n = len(x)


# 1. Линейная аппроксимация (y = a + b * x)
def linear_approximation(x, y):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_xy = np.sum(x * y)

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    y_pred = a + b * x
    # Суммарная погрешность
    error = np.sum((y - y_pred) ** 2)

    return np.round(a, 2), np.round(b, 2), error


# 2. Степенная аппроксимация (y = a * x^b)
def power_approximation(x, y):
    ln_x = np.log(x)
    ln_y = np.log(y)

    sum_ln_x = np.sum(ln_x)
    sum_ln_y = np.sum(ln_y)
    sum_ln_x2 = np.sum(ln_x ** 2)
    sum_ln_xy = np.sum(ln_x * ln_y)

    b = (n * sum_ln_xy - sum_ln_x * sum_ln_y) / (n * sum_ln_x2 - sum_ln_x ** 2)
    ln_a = (sum_ln_y - b * sum_ln_x) / n
    a = np.exp(ln_a)

    y_pred = a * x ** b
    # Суммарная погрешность
    error = np.sum((y - y_pred) ** 2)

    return np.round(a, 2), np.round(b, 2), error


# 3. Показательная аппроксимация (y = a * exp(b * x))
def exponential_approximation(x, y):
    ln_y = np.log(y)

    sum_x = np.sum(x)
    sum_ln_y = np.sum(ln_y)
    sum_x2 = np.sum(x ** 2)
    sum_x_ln_y = np.sum(x * ln_y)

    b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x ** 2)
    ln_a = (sum_ln_y - b * sum_x) / n
    a = np.exp(ln_a)

    y_pred = a * np.exp(b * x)
    # Суммарная погрешность
    error = np.sum((y - y_pred) ** 2)

    return np.round(a, 2), np.round(b, 2), error


# 4. Квадратичная аппроксимация (y = a * x^2 + b * x + c)
def quadratic_approximation(x, y):
    sum_x = np.sum(x)
    sum_x2 = np.sum(x ** 2)
    sum_x3 = np.sum(x ** 3)
    sum_x4 = np.sum(x ** 4)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum(x ** 2 * y)

    A = np.array([[sum_x4, sum_x3, sum_x2],
                  [sum_x3, sum_x2, sum_x],
                  [sum_x2, sum_x, n]])

    B = np.array([sum_x2y, sum_xy, sum_y])

    a, b, c = np.linalg.solve(A, B)

    y_pred = a * x ** 2 + b * x + c
    # Суммарная погрешность
    error = np.sum((y - y_pred) ** 2)

    return np.round(a, 2), np.round(b, 2), np.round(c, 2), error


# Получение параметров для каждой аппроксимации
a_lin, b_lin, error_lin = linear_approximation(x, y)
a_pow, b_pow, error_pow = power_approximation(x, y)
a_exp, b_exp, error_exp = exponential_approximation(x, y)
a_quad, b_quad, c_quad, error_quad = quadratic_approximation(x, y)

# Построение графиков
x_line = np.linspace(min(x), max(x), 100)

# Вычисление значений по аппроксимациям
y_linear = a_lin + b_lin * x_line
y_power = a_pow * x_line ** b_pow
y_exp = a_exp * np.exp(b_exp * x_line)
y_quad = a_quad * x_line ** 2 + b_quad * x_line + c_quad

# Сравнение результатов
print(f"Линейная аппроксимация: y = {a_lin} + {b_lin} * x, Суммарная погрешность: {error_lin:.4f}")
print(f"Степенная аппроксимация: y = {a_pow} * x^{b_pow}, Суммарная погрешность: {error_pow:.4f}")
print(f"Показательная аппроксимация: y = {a_exp} * exp({b_exp} * x), Суммарная погрешность: {error_exp:.4f}")
print(f"Квадратичная аппроксимация: y = {a_quad} * x^2 + {b_quad} * x + {c_quad}, Суммарная погрешность: {error_quad:.4f}")

# Построение графиков
plt.scatter(x, y, color='red', label='Экспериментальные точки')

plt.plot(x_line, y_linear, color='blue', label=f'Линейная: {a_lin} + {b_lin} * x')
plt.plot(x_line, y_power, color='green', label=f'Степенная: {a_pow} * x^{b_pow}')
plt.plot(x_line, y_exp, color='orange', label=f'Показательная: {a_exp} * exp({b_exp} * x)')
plt.plot(x_line, y_quad, color='purple', label=f'Квадратичная: {a_quad} * x^2 + {b_quad} * x + {c_quad}')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Аппроксимация данных')
plt.show()
