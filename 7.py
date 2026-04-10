def print_common_multiples(a, b, n):
    """
    Выводит на экран в порядке возрастания все общие кратные
    для двух натуральных чисел A и B, не превосходящие N.

    Args:
        a: Первое натуральное число
        b: Второе натуральное число
        n: Верхняя граница для общих кратных
    """

    # Проверяем, что все числа натуральные (положительные целые)
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(n, int)):
        raise TypeError("Все аргументы должны быть целыми числами")

    if a <= 0 or b <= 0 or n <= 0:
        raise ValueError("Числа A, B и N должны быть натуральными (больше 0)")

    # Находим наименьшее общее кратное (НОК) для чисел A и B
    # Сначала находим наибольший общий делитель (НОД) с помощью алгоритма Евклида
    def gcd(x, y):
        """Возвращает наибольший общий делитель чисел x и y"""
        while y != 0:
            x, y = y, x % y
        return x

    # НОК = |a * b| / НОД(a, b)
    lcm = abs(a * b) // gcd(a, b)

    # Находим и выводим все общие кратные, не превосходящие N
    common_multiples = []
    multiple = lcm

    while multiple <= n:
        common_multiples.append(multiple)
        multiple += lcm

    # Выводим результат
    if common_multiples:
        print(f"Общие кратные чисел {a} и {b}, не превосходящие {n}:")
        for num in common_multiples:
            print(num, end=" ")
        print()  # Переход на новую строку
    else:
        print(f"Нет общих кратных чисел {a} и {b}, не превосходящих {n}")


# Более простая версия (без проверок типов)
def print_common_multiples_simple(a, b, n):
    """
    Простая версия функции для вывода общих кратных.
    """
    # Находим наибольшее из чисел для оптимизации
    max_num = max(a, b)

    # Создаем список для хранения общих кратных
    common_multiples = []

    # Перебираем числа от max_num до n
    for i in range(max_num, n + 1):
        if i % a == 0 and i % b == 0:
            common_multiples.append(i)

    # Выводим результат
    if common_multiples:
        print(f"Общие кратные чисел {a} и {b}, не превосходящие {n}:")
        for num in common_multiples:
            print(num, end=" ")
        print()
    else:
        print(f"Нет общих кратных чисел {a} и {b}, не превосходящих {n}")


# Примеры использования
if __name__ == "__main__":
    print("=== Пример 1 ===\n")
    print_common_multiples(4, 6, 50)

    print("\n=== Пример 2 ===\n")
    print_common_multiples(3, 5, 30)

    print("\n=== Пример 3 ===\n")
    print_common_multiples(7, 11, 100)

    print("\n=== Пример 4 ===\n")
    print_common_multiples(8, 12, 20)

    print("\n=== Пример 5 (с простой версией) ===\n")
    print_common_multiples_simple(2, 3, 20)