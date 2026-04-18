def calculate_final_price(price, has_discount_card, is_holiday):
    """
    Рассчитывает итоговую стоимость товара с учётом всех скидок.

    Параметры:
    price - стоимость покупки (float или int)
    has_discount_card - наличие дисконтной карты (bool)
    is_holiday - праздничный ли день (bool)

    Возвращает:
    float - итоговая стоимость с округлением до двух знаков
    """
    if price > 30000:
        base = 10
    elif price > 20000:
        base = 7
    elif price > 15000:
        base = 5
    elif price > 5000:
        base = 3
    else:
        base = 0

    # Суммируем все скидки
    total = base
    total += 5 if has_discount_card else 0
    total += 3 if is_holiday else 0

    # Ограничиваем максимум 15%
    total = min(total, 15)

    return round(price * (100 - total) / 100, 2)

print(calculate_final_price(4000, False, False))
