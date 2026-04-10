def seconds_since_new_year(datetime_str):
    """
    Альтернативная версия с константами.
    """
    # Константа: количество секунд в дне
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    try:
        # Разбор строки
        date_part, time_part = datetime_str.strip().split()
        month, day, year = map(int, date_part.split('/'))
        hour, minute, second = map(int, time_part.split(':'))

        # Проверка данных
        if month < 1 or month > 12:
            raise ValueError("Неверный месяц")

        # Количество дней в месяцах для обычного года
        DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Корректировка для високосного года
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        if is_leap(year):
            DAYS_IN_MONTH[1] = 29

        # Проверка дня
        if day < 1 or day > DAYS_IN_MONTH[month - 1]:
            raise ValueError("Неверный день")

        # Проверка времени
        if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
            raise ValueError("Неверное время")

        # Расчет дней
        days_passed = sum(DAYS_IN_MONTH[:month - 1]) + (day - 1)

        # Расчет секунд
        total_seconds = (days_passed * SECONDS_IN_DAY +
                         hour * SECONDS_IN_HOUR +
                         minute * SECONDS_IN_MINUTE +
                         second)

        return total_seconds

    except (ValueError, IndexError) as e:
        print(f"Ошибка: {e}")
        return None