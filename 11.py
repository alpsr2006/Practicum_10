def is_prime(n):
    """Функция проверяет, является ли число простым.
    
    Параметры:
    n (int) целое число для проверки
    
    Возвращает:
    bool True если число простое, False в противном случае
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Введите N: "))
print(f"Простые числа от 1 до {N}:", end=" ")
for i in range(1, N + 1):
    if is_prime(i):
        print(i, end=" ")
