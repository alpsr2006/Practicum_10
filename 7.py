def print_common_multiples_simple(a, b, n):
    """
    Функция для вывода общих кратных.
    """
    max_num = max(a, b)

    common_multiples = []

    for i in range(max_num, n + 1):
        if i % a == 0 and i % b == 0:
            common_multiples.append(i)

    if common_multiples:
        print(f"Общие кратные чисел {a} и {b}, не превосходящие {n}:")
        for num in common_multiples:
            print(num, end=" ")
        print()
    else:
        print(f"Нет общих кратных чисел {a} и {b}, не превосходящих {n}")
