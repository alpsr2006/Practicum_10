def make_payment(P):
    """
    Проверяет возможность оплаты ежемесячного платежа по кредитной карте.

    Параметры:
    P - сумма платежа (число)

    Возвращает:
    None - только печатает результат
    """

    CREDIT_LIMIT = 1000
    MIN_PAYMENT = 20

    if P < 0:
        print("Ошибка: Сумма платежа не может быть отрицательной")
        return

    if not isinstance(P, (int, float)):
        print("Ошибка: Сумма платежа должна быть числом")
        return

    if P < MIN_PAYMENT:
        print(f"Повторить попытку: Минимальный платеж составляет ${MIN_PAYMENT}")
        return

    if P > CREDIT_LIMIT:
        print(f"Повторить попытку: Сумма платежа превышает кредитный лимит в ${CREDIT_LIMIT}")
        return

    print("Успех")
