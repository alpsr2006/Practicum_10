def print_numbers_with_allowed_digits_math(a, b):
    """
    Версия с использованием математической проверки цифр.
    """
    ALLOWED_DIGITS = {1, 3, 4, 8, 9}

    # Обеспечиваем правильный порядок
    if a > b:
        a, b = b, a
        print(f"Значения заменены. Диапазон: [{a}, {b}]")

    print(f"\nЧисла в диапазоне [{a}, {b}], состоящие из цифр {sorted(ALLOWED_DIGITS)}:")

    found_numbers = []

    def has_only_allowed_digits(n):
        """Проверяет, состоит ли число только из разрешенных цифр"""
        if n == 0:
            return False

        while n > 0:
            digit = n % 10
            if digit not in ALLOWED_DIGITS:
                return False
            n //= 10
        return True

    for num in range(a, b + 1):
        if has_only_allowed_digits(num):
            found_numbers.append(num)

    if found_numbers:
        print(*found_numbers)
        print(f"\nКоличество: {len(found_numbers)}")
    else:
        print("Числа не найдены")