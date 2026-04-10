"""
Программа для создания мозаичного узора кафельной плитки
Особенности:
- треугольники, собранные в квадратные модули
- градиент от светло-голубого к темно-синему
- симметричный узор с расходящимися лучами от центра
- белые швы между элементами
"""

import turtle as t
import math

# ==================== НАСТРОЙКА ОКНА ====================
t.setup(900, 900)
t.bgcolor("#f5f5f5")  # Светлый фон для контраста
t.speed(0)
t.hideturtle()
t.pensize(1)
t.tracer(0)


# ==================== ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ====================
def go(x, y):
    """Перемещает черепашку в указанные координаты"""
    t.penup()
    t.goto(x, y)
    t.pendown()


# ==================== 1. ФУНКЦИЯ РИСОВАНИЯ ТРЕУГОЛЬНИКА ====================
def triangle(x1, y1, x2, y2, x3, y3, color):
    """
    Рисует треугольник по координатам трех вершин с заданным цветом заливки
    """
    t.pencolor("white")  # Белые швы между элементами
    t.fillcolor(color)
    go(x1, y1)
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()


# ==================== 2. ФУНКЦИЯ РИСОВАНИЯ КВАДРАТА ИЗ ДВУХ ТРЕУГОЛЬНИКОВ ====================
def square_module(x, y, size, color1, color2, diag=0):
    """
    Рисует квадрат из двух треугольников
    x, y — левый нижний угол квадрата
    size — сторона квадрата
    color1, color2 — цвета двух треугольников
    diag = 0 — диагональ из левого нижнего в правый верхний (/)
    diag = 1 — диагональ из левого верхнего в правый нижний (\)
    """
    if diag == 0:
        # диагональ из левого нижнего в правый верхний (/)
        triangle(x, y, x + size, y, x + size, y + size, color1)
        triangle(x, y, x, y + size, x + size, y + size, color2)
    else:
        # диагональ из левого верхнего в правый нижний (\)
        triangle(x, y, x + size, y, x, y + size, color1)
        triangle(x + size, y, x + size, y + size, x, y + size, color2)


# ==================== 3. ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ГРАДИЕНТА ====================
def get_gradient_color(distance, max_distance):
    """
    Возвращает цвет в зависимости от расстояния до центра
    Создает плавный переход от светло-голубого к темно-синему

    distance: расстояние от центра (0 - центр, max_distance - край)
    max_distance: максимальное расстояние
    """
    # Нормализуем расстояние (0 - центр, 1 - край)
    t_param = min(1.0, distance / max_distance)

    # Создаем плавный переход от светлого к темному
    # Светлый цвет (центр): RGB(200, 225, 255)
    # Темный цвет (край): RGB(20, 40, 80)

    r = int(200 - t_param * 180)
    g = int(225 - t_param * 185)
    b = int(255 - t_param * 175)

    # Добавляем насыщенность для темных тонов
    if t_param > 0.7:
        r = max(20, r - 10)
        g = max(40, g - 10)
        b = max(80, b - 5)

    return f"#{r:02x}{g:02x}{b:02x}"


# ==================== 4. ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ЛУЧЕВОГО УЗОРА ====================
def get_diagonal_direction(row, col, center_row, center_col):
    """
    Определяет направление диагонали для создания лучевого узора
    Лучи расходятся от центра
    """
    # Определяем угол относительно центра
    angle = math.atan2(row - center_row, col - center_col)

    # Разбиваем на 4 сектора
    if -math.pi / 4 <= angle < math.pi / 4:
        # Правый сектор
        return (row + col) % 2
    elif math.pi / 4 <= angle < 3 * math.pi / 4:
        # Верхний сектор
        return (row - col) % 2
    elif -3 * math.pi / 4 <= angle < -math.pi / 4:
        # Нижний сектор
        return (col - row) % 2
    else:
        # Левый сектор
        return (row + col + 1) % 2


# ==================== 5. ОСНОВНАЯ ФУНКЦИЯ: УЗОР КАФЕЛЬНОЙ ПЛИТКИ ====================
def tile_pattern(rows, cols, size):
    """
    Создает узор кафельной плитки с градиентом от центра
    rows: количество строк
    cols: количество столбцов
    size: размер одной плитки
    """
    # Вычисляем начальные координаты для центрирования
    start_x = -cols * size / 2
    start_y = -rows * size / 2

    # Определяем центр композиции
    center_row = rows / 2 - 0.5
    center_col = cols / 2 - 0.5

    # Максимальное расстояние от центра (для градиента)
    max_distance = math.sqrt(center_row ** 2 + center_col ** 2) * 1.2

    # Рисуем каждый квадратный модуль
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * size
            y = start_y + row * size

            # Вычисляем расстояние от центра
            distance = math.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)

            # Получаем цвета для треугольников (градиент от центра)
            color_light = get_gradient_color(distance, max_distance)
            color_dark = get_gradient_color(distance * 1.2, max_distance)

            # Для создания выразительного рисунка, темный треугольник
            # всегда направлен от центра
            angle = math.atan2(row - center_row, col - center_col)

            # Определяем направление диагонали для создания лучевого узора
            if abs(row - center_row) < 0.5 and abs(col - center_col) < 0.5:
                # Центральный модуль
                diag = 0
                color1 = get_gradient_color(0, max_distance)  # Самый светлый
                color2 = get_gradient_color(0.1, max_distance)
            else:
                # Определяем сектор для лучевого узора
                if abs(angle) < math.pi / 4:
                    # Правый сектор
                    diag = 1
                    color1 = color_light
                    color2 = color_dark
                elif abs(angle - math.pi / 2) < math.pi / 4:
                    # Верхний сектор
                    diag = 0
                    color1 = color_dark
                    color2 = color_light
                elif abs(angle + math.pi / 2) < math.pi / 4:
                    # Нижний сектор
                    diag = 1
                    color1 = color_dark
                    color2 = color_light
                else:
                    # Левый сектор
                    diag = 0
                    color1 = color_light
                    color2 = color_dark

            # Рисуем квадратный модуль
            square_module(x, y, size, color1, color2, diag)


# ==================== 6. ДОПОЛНИТЕЛЬНАЯ ФУНКЦИЯ: УЗОР С РАСХОДЯЩИМИСЯ ЛУЧАМИ ====================
def tile_pattern_radial(rows, cols, size):
    """
    Создает узор с выраженными лучами, расходящимися от центра
    """
    start_x = -cols * size / 2
    start_y = -rows * size / 2

    center_row = rows / 2 - 0.5
    center_col = cols / 2 - 0.5
    max_distance = math.sqrt(center_row ** 2 + center_col ** 2)

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * size
            y = start_y + row * size

            # Расстояние и угол от центра
            distance = math.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)
            angle = math.atan2(row - center_row, col - center_col)

            # Интенсивность цвета (темнее на краях)
            intensity = min(1.0, distance / max_distance)

            # Светлые цвета в центре
            if intensity < 0.3:
                r = int(180 + 75 * intensity)
                g = int(210 + 45 * intensity)
                b = int(245 + 10 * intensity)
            elif intensity < 0.7:
                r = int(100 + 80 * (intensity - 0.3) / 0.4)
                g = int(140 + 70 * (intensity - 0.3) / 0.4)
                b = int(200 + 55 * (intensity - 0.3) / 0.4)
            else:
                r = int(30 + 70 * (intensity - 0.7) / 0.3)
                g = int(50 + 90 * (intensity - 0.7) / 0.3)
                b = int(80 + 120 * (intensity - 0.7) / 0.3)

            color1 = f"#{r:02x}{g:02x}{b:02x}"

            # Второй цвет - более темный оттенок
            r2 = max(20, r - 40)
            g2 = max(40, g - 40)
            b2 = max(60, b - 40)
            color2 = f"#{r2:02x}{g2:02x}{b2:02x}"

            # Направление диагонали зависит от угла (лучевой узор)
            sector = int((angle + math.pi) / (math.pi / 4)) % 8

            if sector in [0, 4]:
                diag = 0
            elif sector in [1, 5]:
                diag = 1
            elif sector in [2, 6]:
                diag = 0
            else:
                diag = 1

            # Чередуем цвета для создания эффекта лучей
            if sector % 2 == 0:
                square_module(x, y, size, color1, color2, diag)
            else:
                square_module(x, y, size, color2, color1, diag)


# ==================== 7. ЗАПУСК ПРОГРАММЫ ====================
def main():
    """
    Главная функция для выбора и отображения узора
    """
    # Параметры узора
    ROWS = 12  # Количество строк
    COLS = 12  # Количество столбцов
    TILE_SIZE = 65  # Размер одной плитки

    # Выберите один из узоров:

    # Узор 1: Классический с плавным градиентом
    tile_pattern(ROWS, COLS, TILE_SIZE)

    # Узор 2: С выраженными расходящимися лучами (раскомментируйте для использования)
    # tile_pattern_radial(ROWS, COLS, TILE_SIZE)

    t.update()
    t.exitonclick()


if __name__ == "__main__":
    main()