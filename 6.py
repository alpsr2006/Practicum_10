def check_sms_length(message):
    """
    Проверяет длину сообщения и возвращает его целиком или первые 160 символов.

    Args:
        message: Текст сообщения (строка)

    Returns:
        str: Сообщение целиком (если длина <= 160) или первые 160 символов
    """

    # Константа максимальной длины SMS
    MAX_SMS_LENGTH = 160

    # Проверяем длину сообщения
    if len(message) <= MAX_SMS_LENGTH:
        # Если длина не превышает лимит, возвращаем сообщение целиком
        return message
    else:
        # Если длина превышает лимит, возвращаем первые 160 символов
        return message[:MAX_SMS_LENGTH]


# Примеры использования функции
if __name__ == "__main__":
    # Пример 1: Короткое сообщение
    short_message = "Привет! Как дела?"
    result1 = check_sms_length(short_message)
    print(f"Сообщение: '{short_message}'")
    print(f"Длина: {len(short_message)} символов")
    print(f"Результат: '{result1}'")
    print(f"Длина результата: {len(result1)} символов\n")

    # Пример 2: Длинное сообщение
    long_message = "Это очень длинное сообщение, которое превышает лимит в 160 символов. " * 3
    result2 = check_sms_length(long_message)
    print(f"Длина исходного сообщения: {len(long_message)} символов")
    print(f"Результат: '{result2}'")
    print(f"Длина результата: {len(result2)} символов\n")

    # Пример 3: Сообщение ровно 160 символов
    exact_message = "A" * 160
    result3 = check_sms_length(exact_message)
    print(f"Длина исходного сообщения: {len(exact_message)} символов")
    print(f"Результат: '{result3}'")
    print(f"Длина результата: {len(result3)} символов\n")

    # Пример 4: Пустое сообщение
    empty_message = ""
    result4 = check_sms_length(empty_message)
    print(f"Сообщение: '{empty_message}'")
    print(f"Длина: {len(empty_message)} символов")
    print(f"Результат: '{result4}'")
    print(f"Длина результата: {len(result4)} символов")