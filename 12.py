import turtle

def draw_rhombus(x, y, size, fill_color, pen_color):
    """Рисует ромб с центром в координатах (x, y)
    x - "Координата по горизонтали (ось X) центра ромба"
    y - "Координата по вертикали (ось Y) центра ромба"
    size - "Расстояние от центра до любой вершины ромба (половина диагонали)
    fill_color - "Цвет заливки внутренней области ромба"
    pen_color - "Цвет контура (линий) ромба"""
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

def draw_flower(x, y, radius, fill_color):
    """Рисует стилизованный четырехлистник из дуг с центром в (x,y)
    x - "Координата по горизонтали (ось X) центра цветка"
    y - "Координата по вертикали (ось Y) центра цветка"
    radius - "Радиус дуг, из которых состоят лепестки цветка (определяет размер цветка)"
    fill_color - "Цвет заливки лепестков цветка"""
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

def draw_circle(x, y, radius, fill_color):
    """Рисует круг (сердцевину) точно по центру координат (x,y)"""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("white", fill_color)

    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=300)
    screen.bgcolor("#1A1A1A")  # Темно-серый фон для контраста
    screen.title("Цветной графический орнамент")

    turtle.speed(0)
    turtle.hideturtle()  # Скрываем саму черепашку
    turtle.pensize(2)

    start_x = -300
    y_pos = 0
    step = 100  # Расстояние между центрами основных элементов
    num_elements = 7  # Количество повторений

    for i in range(num_elements):
        current_x = start_x + (i * step)

        draw_rhombus(current_x, y_pos, 50, "#8B0000", "#FF4500")

        draw_flower(current_x, y_pos, 35, "#FFD700")

        draw_circle(current_x, y_pos, 10, "#000080")

        # маленький ромб между основными
        if i < num_elements - 1:  # Не рисуем после последнего элемента
            draw_rhombus(current_x + 50, y_pos, 15, "#228B22", "#32CD32")  # Зеленый

    turtle.done()

if name == "__main__":
    main()
