import cmath  # Для работы с комплексными числами
import numpy as np

# Машинное эпсилон
epsilon = np.finfo(float).eps

def cardano(a, b, c):
    """
    Решение кубического уравнения методом Кардано.
    x^3 + a*x^2 + b*x + c = 0
    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный член
    :return: три корня уравнения
    """
    # Приведение к форме y^3 + p*y + q = 0
    p = b - a ** 2 / 3
    q = c - a * b / 3 + 2 * (a / 3) ** 2

    # Вычисление дискриминанта
    s = cmath.sqrt((p / 3) ** 3 + (q / 2) ** 2)

    # Один действительный корень y1
    y1 = (-(q / 2) + s) ** (1 / 3) + (-(q / 2) - s) ** (1 / 3)

    # Возвращаем корень исходного уравнения
    x1 = y1 - a / 3

    # Разделяем кубическое уравнение на (x - x1) и решаем квадратное
    a1 = 1
    b1 = a + x1
    c1 = b + x1 * b1
    discriminant = b1 ** 2 - 4 * a1 * c1

    # Находим оставшиеся два корня
    x2 = (-b1 + cmath.sqrt(discriminant)) / (2 * a1)
    x3 = (-b1 - cmath.sqrt(discriminant)) / (2 * a1)

    return [x1, x2, x3]

def cardano_error_analysis(alpha_values):
    """
    Исследование потери точности метода Кардано.
    :param alpha_values: список значений α для анализа
    """
    results = []
    for alpha in alpha_values:
        # Коэффициенты уравнения
        a = 3
        b = alpha ** 2
        c = alpha ** 2

        # Применяем метод Кардано
        try:
            roots = cardano(a, b, c)

            # Перепроверим результат: Подставляем корни обратно в уравнение
            residuals = [abs(x ** 3 + a * x ** 2 + b * x + c) for x in roots]

            # Записываем результат
            results.append((alpha, roots, residuals))
        except Exception as e:
            results.append((alpha, None, str(e)))

    # Выводим результаты
    for alpha, roots, residuals in results:
        print(f"α = {alpha}")
        if roots is not None:
            print(f"Корни: {roots}")
            print(f"Остатки (ошибки): {residuals}")
        else:
            print(f"Ошибка: {residuals}")
        print("-" * 50)

def f(x, alpha):
    return x**3 + 3 * x**2 + alpha**2 * x + alpha**2

def f_prime(x, alpha):
    return 3 * x**2 + 6 * x + alpha**2

def newton(alpha, x0, tol=1e-10, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x, alpha)
        fpx = f_prime(x, alpha)
        if abs(fpx) < 1e-12:
            raise ValueError("Производная близка к нулю")
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Метод Ньютона не сошёлся")


def newton_error_analysis(alpha_values, initial_guesses):
    """
    Исследование влияния ошибок округления и выбора начального приближения в методе Ньютона.
    :param alpha_values: список значений α для анализа
    :param initial_guesses: список начальных приближений
    """
    results = []
    for alpha in alpha_values:
        for x0 in initial_guesses:
            try:
                root = newton(alpha, x0)

                # Перепроверим результат: Подставляем корень обратно в уравнение
                residual = abs(f(root, alpha))

                # Записываем результат
                results.append((alpha, x0, root, residual))
            except Exception as e:
                results.append((alpha, x0, None, str(e)))

    # Выводим результаты
    for alpha, x0, root, residual in results:
        print(f"α = {alpha}, Начальное приближение: {x0}")
        if root is not None:
            print(f"Найденный корень: {root}")
            print(f"Остаток (ошибка): {residual}")
        else:
            print(f"Ошибка: {residual}")
        print("-" * 50)


print("Метод Кардано")
alpha_values = [10**-5, 10**0, 10**5, 10**10, 10**12]
cardano_error_analysis(alpha_values)
print()
print("Метод Ньютона")
initial_guesses = [-10, 0, 10]
alpha_values = [10**-5, 10**0, 10**5, 10**10, 10**12]

for alpha in alpha_values:
    for x0 in initial_guesses:
        try:
            root = newton(alpha, x0)
            print(f"α = {alpha}, Начальное приближение: {x0}, Корень: {root}")
        except Exception as e:
            print(f"α = {alpha}, Начальное приближение: {x0}, Ошибка: {e}")
