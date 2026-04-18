import turtle

def triangle(x, y, leg_hor, leg_vert, color):
    """x - "Координата по горизонтали (ось X) вершины прямого угла"
    y - "Координата по вертикали (ось Y) вершины прямого угла"
    leg_hor - "Длина горизонтального катета (со знаком + вправо, - влево)"
    leg_vert - "Длина вертикального катета (со знаком + вверх, - вниз)"
    color - "Цвет заливки внутренней области треугольника"""
    turtle.pensize(5)
    turtle.color('black', color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(leg_hor)
    turtle.left(90)
    turtle.forward(leg_vert)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.up()

def square(x, y, dark_color, light_color, is_dark_bottom_left):
    size = 50
    if is_dark_bottom_left:
        triangle(x, y, size, -size, dark_color)
        triangle(x + size, y - size, -size, size, light_color)
    else:
        triangle(x, y - size, size, size, light_color)
        triangle(x + size, y, -size, -size, dark_color)

# Исходная секция (левая верхняя)
original = [
    [0, 0, '#1a66ad', '#61b3ff', True],
    [0, -50, '#61b3ff', '#c7e4ff', True],
    [0, -100, '#c7e4ff', '#61b3ff', True],

    [50, 0, '#61b3ff', '#1a66ad', True],
    [50, -50, '#1a66ad', '#61b3ff', True],
    [50, -100, '#61b3ff', '#c7e4ff', True],

    [100, 0, '#c7e4ff', '#61b3ff', True],
    [100, -50, '#61b3ff', '#1a66ad', True],
    [100, -100, '#1a66ad', '#61b3ff', True]
]

base_x = -150
base_y = 150
size = 50
turtle.speed(600)
# Левая верхняя (исходная)
for x_off, y_off, dark, light, diag in original:
    square(base_x + x_off, base_y + y_off, dark, light, diag)

# Правая верхняя (отражение по горизонтали)
for x_off, y_off, dark, light, diag in original:
    new_x_off = 100 - x_off
    new_diag = not diag
    square(base_x + 150 + new_x_off, base_y + y_off, dark, light, new_diag)

# Левая нижняя (отражение по вертикали)
for x_off, y_off, dark, light, diag in original:
    # Меняем Y: верх становится низом
    if y_off == 0:
        new_y_off = -100
    elif y_off == -50:
        new_y_off = -50
    elif y_off == -100:
        new_y_off = 0

    new_diag = not diag
    # При отражении по вертикали тёмный и светлый цвета меняются местами
    square(base_x + x_off, base_y - 150 + new_y_off, light, dark, new_diag)

# Правая нижняя (отражение по горизонтали и вертикали)
for x_off, y_off, dark, light, diag in original:
    new_x_off = 100 - x_off

    if y_off == 0:
        new_y_off = -100
    elif y_off == -50:
        new_y_off = -50
    elif y_off == -100:
        new_y_off = 0

    # Два отражения - диагональ остаётся, но цвета меняются местами
    square(base_x + 150 + new_x_off, base_y - 150 + new_y_off, light, dark, diag)

turtle.done()
