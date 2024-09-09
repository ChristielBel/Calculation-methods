import math

# Полный ряд для больших x
def s_full(x, tolerance=8e-3):
    sum_s = 0.0
    k = 1
    while True:
        term1 = 1 / math.sqrt(k**3 + x)
        term2 = 1 / math.sqrt(k**3 - x)
        term = term1 - term2
        if abs(term) < tolerance:
            break
        sum_s += term
        k += 1
    return sum_s

# Быстрое приближение для малых x
def s_approx(x):
    zeta_4 = math.pi**4 / 90
    return x * zeta_4

# Основная функция
def s_x(x):
    if abs(x) < 0.1:
        return s_approx(x)
    else:
        return s_full(x)

# Вычисление для x = 0.5 и x = 0.999999999
x1 = 0.5
x2 = 0.999999999
print(f"s({x1}) = {s_x(x1)}")
print(f"s({x2}) = {s_x(x2)}")
