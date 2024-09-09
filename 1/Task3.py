import math

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

def s_approx(x):
    zeta_4 = math.pi**4 / 90
    return x * zeta_4

# Вычисление для x = 0.5 и x = 0.999999999
x_values = [0.5, 0.999999999]
for x in x_values:
    result_exact = s_full(x)
    result_fast = s_approx(x)
    print(f"x = {x}, s(x) = {result_exact:.8f}")
    print(f"x = {x}, s(x) (быстрый метод) = {result_fast:.8f}")
