import math

# Первые два члена
pi_sq_over_6 = math.pi**2 / 6
pi_4_over_90 = math.pi**4 / 90

# Вычисление суммы ряда 1/n^4(n^2 + 1)
def remainder_series(tolerance=1e-10):
    sum_remainder = 0.0
    n = 1
    while True:
        term = 1 / (n**4 * (n**2 + 1))
        if term < tolerance:
            break
        sum_remainder += term
        n += 1
    return sum_remainder

# Полная сумма
def full_sum():
    remainder = remainder_series()
    return pi_sq_over_6 - pi_4_over_90 + remainder

# Вычисление
result = full_sum()
print(f"Сумма ряда: {result:.10f}")
