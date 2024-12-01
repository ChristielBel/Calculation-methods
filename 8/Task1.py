import math


def erf(x, n=1000):
    if n % 2 == 1:
        n += 1  

    def f(t):
        return math.exp(-t ** 2)

    h = x / n
    integral = f(0) + f(x) 

    for i in range(1, n, 2):
        integral += 4 * f(i * h)
    for i in range(2, n, 2):
        integral += 2 * f(i * h)

    integral *= h / 3
    return (2 / math.sqrt(math.pi)) * integral

x1, x2 = 0.5, 0.0
result = erf(x1) - erf(x2)
print(erf(x1),erf(x2))
print(f"Результат: erf(0.5) - erf(0.0) = {result}")
