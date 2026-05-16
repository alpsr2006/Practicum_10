def print_fibonacci_numbers(n):
    """Функция выводит первые n чисел последовательности Фибоначчи.
    
    Параметры:
    n (int) количество чисел Фибоначчи для вывода
    
    Возвращает:
    None функция выводит результат на экран, но ничего не возвращает
    """
    if n <= 0:
        return

    fib_sequence = []

    for position in range(n):
        if position == 0 or position == 1:
            fib_sequence.append(1)
        else:
            fib_sequence.append(fib_sequence[position-1]
                                + fib_sequence[position-2])

    print(' '.join(map(str, fib_sequence)))

print_fibonacci_numbers(7)

