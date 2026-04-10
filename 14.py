"""
Функции для поиска подстроки в строке ДНК (символы A, T, C, G)
Реализация алгоритма Бойера-Мура для эффективного поиска
"""

# функция первого вхождения

def find_substring(string, substring, start=0, end=None):
    """
    Возвращает индекс первого вхождения подстроки в строке.
    Работает аналогично методу str.find().

    Аргументы:
        string: строка, в которой ведется поиск
        substring: подстрока, которую нужно найти
        start: позиция начала поиска (по умолчанию 0)
        end: позиция окончания поиска (по умолчанию len(string))

    Возвращает:
        int: индекс первого вхождения или -1, если подстрока не найдена
    """
    # Обработка границ
    if end is None:
        end = len(string)

    # Проверка корректности границ
    if start < 0:
        start = 0
    if end > len(string):
        end = len(string)

    # Если подстрока пустая, возвращаем start
    if not substring:
        return start

    # Если подстрока длиннее искомого участка
    if len(substring) > end - start:
        return -1

    # Построение таблицы смещений для алгоритма Бойера-Мура
    def build_shift_table(pattern):
        """Создает таблицу смещений для алгоритма Бойера-Мура"""
        table = {}
        pattern_len = len(pattern)

        # Для каждого символа в pattern (кроме последнего)
        for i in range(pattern_len - 1):
            # Смещение = длина pattern - i - 1
            table[pattern[i]] = pattern_len - i - 1

        return table

    pattern = substring
    text = string[start:end]
    pattern_len = len(pattern)
    text_len = len(text)

    # Если pattern пустой
    if pattern_len == 0:
        return start

    # Построение таблицы смещений
    shift_table = build_shift_table(pattern)

    # Алгоритм Бойера-Мура
    i = pattern_len - 1  # индекс в тексте
    while i < text_len:
        k = 0  # количество совпавших символов
        j = pattern_len - 1  # индекс в pattern

        # Сравниваем символы с конца
        while j >= 0 and text[i - k] == pattern[j]:
            k += 1
            j -= 1

        # Если нашли совпадение
        if j < 0:
            return start + (i - pattern_len + 1)

        # Иначе вычисляем смещение
        # Получаем символ, на котором произошло несовпадение
        bad_char = text[i - k]

        # Смещение по правилу плохого символа
        if bad_char in shift_table:
            shift = shift_table[bad_char] - k
        else:
            shift = pattern_len - k

        # Смещаемся
        i += max(shift, 1)

    return -1


# ==================== УПРОЩЕННАЯ ВЕРСИЯ (ДЛЯ ПОНИМАНИЯ) ====================

def find_substring_simple(string, substring, start=0, end=None):
    """
    Упрощенная версия поиска (линейный поиск).
    Используется для понимания логики, но менее эффективна.
    """
    if end is None:
        end = len(string)

    if not substring:
        return start

    if len(substring) > end - start:
        return -1

    for i in range(start, end - len(substring) + 1):
        # Проверяем совпадение
        match = True
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            return i

    return -1


# функция поиска всех вхождений

def find_all_occurrences(string, substring):
    """
    Возвращает строку со всеми индексами вхождений подстроки,
    разделенными запятыми.

    Аргументы:
        string: строка, в которой ведется поиск
        substring: подстрока, которую нужно найти

    Возвращает:
        str: индексы вхождений через запятую или пустую строку
    """
    if not substring:
        return ""

    indices = []
    start = 0

    while True:
        # Ищем следующее вхождение
        index = find_substring(string, substring, start)

        if index == -1:
            break

        indices.append(str(index))
        # Продолжаем поиск после найденного индекса
        start = index + 1

    return ",".join(indices)


# функция всех вхождений (с перекрытием)

def find_all_occurrences_overlap(string, substring):
    """
    Возвращает строку со всеми индексами вхождений подстроки,
    включая перекрывающиеся вхождения.

    Например: string = "AAAA", substring = "AA"
    Результат: "0,1,2"
    """
    if not substring:
        return ""

    indices = []
    start = 0

    while True:
        index = find_substring(string, substring, start)

        if index == -1:
            break

        indices.append(str(index))
        # Продолжаем поиск со следующего символа (для перекрытий)
        start = index + 1

    return ",".join(indices)


# функция для работы с днк

def analyze_dna_sequence(dna_string, pattern):
    """
    Анализирует последовательность ДНК и находит все вхождения паттерна.

    Аргументы:
        dna_string: строка ДНК (символы A, T, C, G)
        pattern: искомая последовательность

    Возвращает:
        dict: словарь с результатами поиска
    """
    # Проверка на допустимые символы
    valid_chars = set("ATCG")
    invalid_chars = set(dna_string.upper()) - valid_chars
    if invalid_chars:
        return {
            "error": f"Недопустимые символы в ДНК: {invalid_chars}",
            "first_occurrence": -1,
            "all_occurrences": ""
        }

    dna = dna_string.upper()
    pattern = pattern.upper()

    # Проверка паттерна
    invalid_pattern = set(pattern) - valid_chars
    if invalid_pattern:
        return {
            "error": f"Недопустимые символы в паттерне: {invalid_pattern}",
            "first_occurrence": -1,
            "all_occurrences": ""
        }

    # Поиск первого вхождения
    first = find_substring(dna, pattern)

    # Поиск всех вхождений
    all_occ = find_all_occurrences(dna, pattern)

    return {
        "dna_length": len(dna),
        "pattern_length": len(pattern),
        "first_occurrence": first,
        "all_occurrences": all_occ,
        "count": len(all_occ.split(",")) if all_occ else 0
    }


def test_functions():
    """Тестирование функций поиска"""

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ ПОИСКА ПОДСТРОКИ")
    print("=" * 60)

    # Тест 1: Базовый поиск
    print("\n1. Базовый поиск:")
    text = "ATCGGCTAGCTAGCTAGCTAGC"
    sub = "GCTA"
    result = find_substring(text, sub)
    print(f"   Текст: {text}")
    print(f"   Подстрока: {sub}")
    print(f"   Индекс первого вхождения: {result}")
    print(f"   Проверка через str.find(): {text.find(sub)}")

    # Тест 2: Поиск с start и end
    print("\n2. Поиск с параметрами start и end:")
    text = "ATCGGCTAGCTAGCTAGCTAGC"
    sub = "GCTA"
    result = find_substring(text, sub, start=5, end=15)
    print(f"   Текст: {text}")
    print(f"   Подстрока: {sub}, start=5, end=15")
    print(f"   Результат: {result}")
    print(f"   Проверка через str.find(): {text.find(sub, 5, 15)}")

    # Тест 3: Подстрока не найдена
    print("\n3. Подстрока не найдена:")
    text = "ATCGGCTAGCTAGCTAGCTAGC"
    sub = "XYZ"
    result = find_substring(text, sub)
    print(f"   Текст: {text}")
    print(f"   Подстрока: {sub}")
    print(f"   Результат: {result}")

    # Тест 4: Поиск всех вхождений
    print("\n4. Поиск всех вхождений:")
    text = "ATCGATCGATCG"
    sub = "ATCG"
    result = find_all_occurrences(text, sub)
    print(f"   Текст: {text}")
    print(f"   Подстрока: {sub}")
    print(f"   Все вхождения: {result}")

    # Тест 5: Перекрывающиеся вхождения
    print("\n5. Перекрывающиеся вхождения:")
    text = "AAAAAA"
    sub = "AA"
    result = find_all_occurrences_overlap(text, sub)
    print(f"   Текст: {text}")
    print(f"   Подстрока: {sub}")
    print(f"   Все вхождения (с перекрытиями): {result}")

    # Тест 6: Анализ ДНК
    print("\n6. Анализ последовательности ДНК:")
    dna = "ATCGGCTAGCTAGCTAGCTAGCGGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCT"
    pattern = "GCTA"
    analysis = analyze_dna_sequence(dna, pattern)
    print(f"   Длина ДНК: {analysis['dna_length']}")
    print(f"   Длина паттерна: {analysis['pattern_length']}")
    print(f"   Первое вхождение: {analysis['first_occurrence']}")
    print(f"   Все вхождения: {analysis['all_occurrences']}")
    print(f"   Количество вхождений: {analysis['count']}")

    # Тест 7: Пустая подстрока
    print("\n7. Пустая подстрока:")
    text = "ATCGGCTA"
    sub = ""
    result = find_substring(text, sub)
    print(f"   Текст: {text}, подстрока: ''")
    print(f"   Результат: {result} (должен быть 0)")


# демонстрация

def demonstrate_boyer_moore():
    """Демонстрация работы алгоритма Бойера-Мура"""

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ АЛГОРИТМА БОЙЕРА-МУРА")
    print("=" * 60)

    text = "ATCGGCTAGCTAGCTAGCTAGC"
    pattern = "GCTA"

    print(f"\nТекст: {text}")
    print(f"Паттерн: {pattern}")
    print(f"\nАлгоритм сравнивает символы с конца паттерна,")
    print(f"что позволяет пропускать больше символов при несовпадении.")

    # Показываем таблицу смещений
    def show_shift_table(pattern):
        table = {}
        pattern_len = len(pattern)
        for i in range(pattern_len - 1):
            table[pattern[i]] = pattern_len - i - 1
        return table

    shift_table = show_shift_table(pattern)
    print(f"\nТаблица смещений для паттерна '{pattern}':")
    for char, shift in shift_table.items():
        print(f"   '{char}' -> смещение {shift}")
    print(f"   Другие символы -> смещение {len(pattern)}")

    # Выполняем поиск
    result = find_substring(text, pattern)
    print(f"\nРезультат поиска: индекс {result}")
    print(f"Проверка: {text[result:result+len(pattern)] if result != -1 else 'не найдено'}")


# ==================== ГЛАВНАЯ ФУНКЦИЯ ====================

def main():
    """Главная функция программы"""

    # Запуск тестов
    test_functions()

    # Демонстрация алгоритма Бойера-Мура
    demonstrate_boyer_moore()

    # Пример для исследования ДНК
    print("\n" + "=" * 60)
    print("ПРИМЕР ИССЛЕДОВАНИЯ ДНК")
    print("=" * 60)

    dna_sequence = "ATCGATCGATCGATCGATCGATCGATCGATCGATCG"
    patterns = ["ATCG", "CGAT", "AAAA", "GATC"]

    for pattern in patterns:
        result = find_substring(dna_sequence, pattern)
        all_occ = find_all_occurrences(dna_sequence, pattern)
        print(f"\nПаттерн '{pattern}':")
        print(f"  Первое вхождение: {result}")
        print(f"  Все вхождения: {all_occ if all_occ else 'не найдены'}")


if __name__ == "__main__":
    main()