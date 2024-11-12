import math

# Определим подынтегральную функцию
def f(t):
    return math.exp(-t**2)

# Реализуем метод прямоугольников для левых, правых и центральных прямоугольников
def left_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n))
    return result * h

def right_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + (i + 1) * h) for i in range(n))
    return result * h

def midpoint_rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + (i + 0.5) * h) for i in range(n))
    return result * h

# Реализуем метод трапеций
def trapezoidal_method(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n))
    return result * h

# Реализуем метод Симпсона
def simpson_method(a, b, n):
    if n % 2 == 1:  # n должно быть четным для метода Симпсона
        n += 1
    h = (b - a) / n
    result = f(a) + f(b) + 4 * sum(f(a + (i + 0.5) * h) for i in range(n)) + 2 * sum(f(a + i * h) for i in range(1, n))
    return result * h / 6

# Функция для расчета erf(x) с использованием различных методов
def erf(x, method, n=1000):
    integral = method(0, x, n)
    return 2 / math.sqrt(math.pi) * integral

# Таблица значений erf(x)
print(" x     |  Left Rect   |  Right Rect  |  Mid Rect    |  Trapezoidal |  Simpson   |  Known Value ")
print("-------|--------------|--------------|--------------|--------------|------------|--------------")
for x in [i * 0.1 for i in range(21)]:
    known_value = math.erf(x)  # известное значение функции
    left_rect = erf(x, left_rectangle_method)
    right_rect = erf(x, right_rectangle_method)
    mid_rect = erf(x, midpoint_rectangle_method)
    trap = erf(x, trapezoidal_method)
    simp = erf(x, simpson_method)
    print(f"{x:5.1f}  | {left_rect:12.8f} | {right_rect:12.8f} | {mid_rect:12.8f} | {trap:12.8f} | {simp:10.8f} | {known_value:12.8f}")
