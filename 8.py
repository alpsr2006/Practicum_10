def convert_datetime(datetime_str):
    """
    Упрощенная версия с основными проверками.
    """
    try:
        date_part, time_part = datetime_str.strip().split()
        month, day, year = map(int, date_part.split('/'))
        hour, minute, second = map(int, time_part.split(':'))

        if month < 1 or month > 12:
            print("Ошибка: Неверный месяц")
            return

        if day < 1 or day > 31:
            print("Ошибка: Неверный день")
            return

        if hour < 0 or hour > 23:
            print("Ошибка: Неверный час")
            return

        if minute < 0 or minute > 59:
            print("Ошибка: Неверные минуты")
            return

        if second < 0 or second > 59:
            print("Ошибка: Неверные секунды")
            return

        # Форматирование даты
        year_short = year % 100
        formatted_date = f"{day:02d}.{month:02d}.{year_short:02d}"

        # Преобразование времени
        if hour == 0:
            hour_12, period = 12, "AM"
        elif hour < 12:
            hour_12, period = hour, "AM"
        elif hour == 12:
            hour_12, period = 12, "PM"
        else:
            hour_12, period = hour - 12, "PM"

        formatted_time = f"{hour_12:02d}:{minute:02d}:{second:02d} {period}"

        print(f"{formatted_date} {formatted_time}")

    except (ValueError, IndexError):
        print("Ошибка: Неверный формат строки. Ожидается: 'MM/DD/YYYY HR:MIN:SEC'")
