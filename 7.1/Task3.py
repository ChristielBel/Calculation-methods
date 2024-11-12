import math

def f(x):
    if 0 <= x <= 2:
        return math.exp(x**2)
    elif 2 < x <= 4:
        return 1 / (4 - math.sin(16 * math.pi * x))
    else:
        raise ValueError("x вне диапазона интегрирования [0, 4]")

# Метод Симпсона
def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)
    return result * h / 3

def calculate_integral():
    # Первый интервал [0, 2]
    a1, b1 = 0, 2
    # Второй интервал (2, 4]
    a2, b2 = 2, 4

    # Число подотрезков для каждого интервала (должно быть четным для метода Симпсона)
    n1, n2 = 1000, 1000

    integral1 = simpson_method(f, a1, b1, n1)
    integral2 = simpson_method(f, a2, b2, n2)

    total_integral = integral1 + integral2
    print(f"Интеграл от 0 до 4 f(x) dx ≈ {total_integral:.10f}")

calculate_integral()
