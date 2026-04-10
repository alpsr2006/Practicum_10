import turtle


# ==========================================
# ФУНКЦИИ ОТРИСОВКИ ГРАФИЧЕСКИХ ЭЛЕМЕНТОВ
# ==========================================

# 1. Геометрический элемент: Ромб
def draw_rhombus(x, y, size, fill_color, pen_color):
    """Рисует ромб с центром в координатах (x, y)"""
    turtle.penup()
    turtle.goto(x, y + size)  # Верхняя точка
    turtle.pendown()
    turtle.color(pen_color, fill_color)

    turtle.begin_fill()
    turtle.goto(x + size, y)  # Правая точка
    turtle.goto(x, y - size)  # Нижняя точка
    turtle.goto(x - size, y)  # Левая точка
    turtle.goto(x, y + size)  # Возврат в верхнюю точку
    turtle.end_fill()


# 2. Растительный элемент: Лепестки (Цветок)
def draw_flower(x, y, radius, fill_color):
    """Рисует стилизованный четырехлистник из дуг с центром в (x,y)"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(45)  # Поворачиваем, чтобы лепестки легли по диагоналям
    turtle.pendown()
    turtle.color("#FFA500", fill_color)  # Оранжевый контур, заданная заливка

    turtle.begin_fill()
    for _ in range(4):
        # Рисуем один лепесток из двух дуг
        turtle.circle(radius, 90)
        turtle.left(90)
        turtle.circle(radius, 90)
        turtle.left(90)
        # Переходим к следующему лепестку
        turtle.right(90)
    turtle.end_fill()
    turtle.setheading(0)  # Сброс угла


# 3. Дополнительный геометрический элемент: Круг
def draw_circle(x, y, radius, fill_color):
    """Рисует круг (сердцевину) точно по центру координат (x,y)"""
    turtle.penup()
    turtle.goto(x, y - radius)  # Смещаемся вниз, чтобы центр был в (x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("white", fill_color)  # Белый контур, заданная заливка

    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# ==========================================
# ОСНОВНАЯ ПРОГРАММА (ПОСТРОЕНИЕ ОРНАМЕНТА)
# ==========================================

def main():
    # Настройка экрана
    screen = turtle.Screen()
    screen.setup(width=800, height=300)
    screen.bgcolor("#1A1A1A")  # Темно-серый фон для контраста
    screen.title("Цветной графический орнамент")

    # Настройка черепашки
    turtle.speed(0)  # Максимальная скорость отрисовки
    turtle.hideturtle()  # Скрываем саму черепашку
    turtle.pensize(2)

    # Параметры орнамента
    start_x = -300
    y_pos = 0
    step = 100  # Расстояние между центрами основных элементов
    num_elements = 7  # Количество повторений

    # Цикл отрисовки повторяющегося орнамента
    for i in range(num_elements):
        current_x = start_x + (i * step)

        # 1. Рисуем фоновый ромб (Темно-красный)
        draw_rhombus(current_x, y_pos, 50, "#8B0000", "#FF4500")

        # 2. Рисуем растительный узор внутри (Золотой)
        draw_flower(current_x, y_pos, 35, "#FFD700")

        # 3. Рисуем сердцевину цветка (Темно-синий)
        draw_circle(current_x, y_pos, 10, "#000080")

        # 4. Соединительный элемент (маленький ромб между основными)
        if i < num_elements - 1:  # Не рисуем после последнего элемента
            draw_rhombus(current_x + 50, y_pos, 15, "#228B22", "#32CD32")  # Зеленый

    # Завершение работы
    turtle.done()


# Запуск программы
if __name__ == "__main__":
    main()