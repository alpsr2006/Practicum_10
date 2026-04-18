def check_sms_length(message):
    """
    Проверяет длину сообщения и возвращает его целиком или первые 160 символов.

    Args:
        message: Текст сообщения (строка)

    Returns:
        str: Сообщение целиком (если длина <= 160) или первые 160 символов
    """

    MAX_SMS_LENGTH = 160

    if len(message) <= MAX_SMS_LENGTH:
        return message
    else:
        return message[:MAX_SMS_LENGTH]
