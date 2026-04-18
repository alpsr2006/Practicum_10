def calculate_card_value():
    """
    Запрашивает у пользователя стоимость карты и возвращает
    денежный эквивалент с учетом бонусов.

    Returns:
        float: Итоговая стоимость карты с бонусом
    """

    CARD_BONUSES = {
        5: 0,  # Карта $5 - без бонуса
        10: 0,  # Карта $10 - без бонуса
        25: 3,  # Карта $25 - бонус $3
        50: 8,  # Карта $50 - бонус $8
        100: 20  # Карта $100 - бонус $20
    }

    # Запрашиваем стоимость карты у пользователя
    while True:
        try:
            card_cost = float(input("Введите стоимость карты "
                                    "(5, 10, 25, 50 или 100): "))

            if card_cost in CARD_BONUSES:
                bonus = CARD_BONUSES[card_cost]
                final_value = card_cost + bonus

                if bonus > 0:
                    print(f"Карта ${card_cost:.0f}: +${bonus} бонуса")
                else:
                    print(f"Карта ${card_cost:.0f}: специальные предложения не предоставляются")

                return final_value
            else:
                print("Ошибка! Допустимые значения: 5, 10, 25, 50, 100")
                print("Пожалуйста, попробуйте снова.\n")

        except ValueError:
            print("Ошибка! Пожалуйста, введите число.\n")


