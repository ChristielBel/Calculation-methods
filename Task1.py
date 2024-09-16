import math


# Функция для решения квадратного уравнения стандартным способом
def solve_quadratic_standard(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  # Уравнение не имеет вещественных корней
    sqrt_discriminant = math.sqrt(discriminant)

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2


# Функция для решения квадратного уравнения альтернативным способом
def solve_quadratic_alternative(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  # Уравнение не имеет вещественных корней
    sqrt_discriminant = math.sqrt(discriminant)

    if b > 0:
        x1 = (-b - sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b - sqrt_discriminant)
    else:
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b + sqrt_discriminant)

    return x1, x2


# Функция для нахождения корней по теореме Виета
def solve_vieta(a, b, c):
    if a == 0:
        return None, None  # Если a = 0, уравнение не квадратное
    x1_plus_x2 = -b / a
    x1_times_x2 = c / a

    # Используем формулу Виета для вычисления корней
    discriminant = x1_plus_x2 ** 2 - 4 * x1_times_x2
    if discriminant < 0:
        return None, None  # Уравнение не имеет вещественных корней

    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (x1_plus_x2 + sqrt_discriminant) / 2
    x2 = (x1_plus_x2 - sqrt_discriminant) / 2

    return x1, x2


# Ввод коэффициентов пользователем
def get_coefficients():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    return a, b, c


# Основная программа
def main():
    a, b, c = get_coefficients()

    # Решение стандартным способом
    x1_standard, x2_standard = solve_quadratic_standard(a, b, c)

    # Решение альтернативным способом
    x1_alternative, x2_alternative = solve_quadratic_alternative(a, b, c)

    # Решение по Виету
    x1_vieta, x2_vieta = solve_vieta(a, b, c)

    print("\nСтандартное решение:")
    if x1_standard is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_standard}, x2 = {x2_standard}")

    print("\nАльтернативное решение:")
    if x1_alternative is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_alternative}, x2 = {x2_alternative}")

    print("\nРешение по Виету:")
    if x1_vieta is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_vieta}, x2 = {x2_vieta}")


if __name__ == "__main__":
    main()
