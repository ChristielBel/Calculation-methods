import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
x = np.array([2, 6, 10, 14, 18, 22])
y = np.array([3.1, 6.7, 9.5, 11.9, 14.0, 15.5])

n = len(x)


# 1. Линейная аппроксимация (y = a + b * x)
def linear_approximation(x, y):
    # ∑y=a⋅n+b⋅∑x
    # ∑(y⋅x)=a⋅∑x+b⋅∑x^2
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_xy = np.sum(x * y)

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    return np.round(a, 2), np.round(b, 2)


# 2. Степенная аппроксимация (y = a * x^b)
def power_approximation(x, y):
    # ln(y)=ln(a)+b⋅ln(x)
    # Здесь аппроксимация становится линейной относительно логарифмов x и y
    # поэтому можно применить метод, аналогичный линейной аппроксимации.
    ln_x = np.log(x)
    ln_y = np.log(y)

    sum_ln_x = np.sum(ln_x)
    sum_ln_y = np.sum(ln_y)
    sum_ln_x2 = np.sum(ln_x ** 2)
    sum_ln_xy = np.sum(ln_x * ln_y)

    b = (n * sum_ln_xy - sum_ln_x * sum_ln_y) / (n * sum_ln_x2 - sum_ln_x ** 2)
    ln_a = (sum_ln_y - b * sum_ln_x) / n
    a = np.exp(ln_a)

    return np.round(a, 2), np.round(b, 2)


# 3. Показательная аппроксимация (y = a * exp(b * x))
def exponential_approximation(x, y):
    # ln(y)=ln(a)+b⋅x
    # Аппроксимация становится линейной относительно ln(y) и x

    ln_y = np.log(y)

    sum_x = np.sum(x)
    sum_ln_y = np.sum(ln_y)
    sum_x2 = np.sum(x ** 2)
    sum_x_ln_y = np.sum(x * ln_y)

    b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x ** 2)
    ln_a = (sum_ln_y - b * sum_x) / n
    a = np.exp(ln_a)

    return np.round(a, 2), np.round(b, 2)


# 4. Квадратичная аппроксимация (y = a * x^2 + b * x + c)
def quadratic_approximation(x, y):
    # ∑y=a⋅∑x^2+b⋅∑x+c⋅n
    # ∑(y⋅x)=a⋅∑x^3+b⋅∑x^2+c⋅∑x
    # ∑(y⋅x^2)=a⋅∑x^4+b⋅∑x^3+c⋅∑x^2

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

    return np.round(a, 2), np.round(b, 2), np.round(c, 2)


# Получение параметров для каждой аппроксимации
a_lin, b_lin = linear_approximation(x, y)
a_pow, b_pow = power_approximation(x, y)
a_exp, b_exp = exponential_approximation(x, y)
a_quad, b_quad, c_quad = quadratic_approximation(x, y)

# Построение графиков
x_line = np.linspace(min(x), max(x), 100)

# Вычисление значений по аппроксимациям
y_linear = a_lin + b_lin * x_line
y_power = a_pow * x_line ** b_pow
y_exp = a_exp * np.exp(b_exp * x_line)
y_quad = a_quad * x_line ** 2 + b_quad * x_line + c_quad

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
plt.title('Аппроксимация')
plt.show()

# Сравнение результатов
print("Линейная аппроксимация: y = {:.2f} + {:.2f} * x".format(a_lin, b_lin))
print("Степенная аппроксимация: y = {:.2f} * x^{:.2f}".format(a_pow, b_pow))
print("Показательная аппроксимация: y = {:.2f} * exp({:.2f} * x)".format(a_exp, b_exp))
print("Квадратичная аппроксимация: y = {:.2f} * x^2 + {:.2f} * x + {:.2f}".format(a_quad, b_quad, c_quad))
