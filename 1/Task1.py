import math


def erf_taylor(x, tolerance=1e-15):
    constant = 2 / math.sqrt(math.pi)

    term = x
    sum_erf = term
    n = 1

    while abs(term) > tolerance:
        term *= -x * x / n
        sum_erf += term / (2 * n + 1)
        n += 1

    return constant * sum_erf


x_values = [0.5, 1.0, 5.0, 10.0]
for x in x_values:
    erf_approx = erf_taylor(x)
    erf_exact = math.erf(x)
    print(
        f"x = {x}, вычисленное {erf_taylor(x)}, точное {erf_exact}, разница {abs(erf_approx - erf_exact)}")
