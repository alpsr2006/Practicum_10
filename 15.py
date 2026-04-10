import turtle as t
import random

# настройка окна
screen = t.Screen()
screen.setup(1000, 700)
screen.bgcolor("#07111f")   # ночное небо
screen.title("Ночной городской пейзаж")

pen = t.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1)

# вспомогательные функции
def go(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def rect(x, y, w, h, color, outline="black"):
    pen.pencolor(outline)
    pen.fillcolor(color)
    go(x, y)
    pen.begin_fill()
    pen.goto(x + w, y)
    pen.goto(x + w, y + h)
    pen.goto(x, y + h)
    pen.goto(x, y)
    pen.end_fill()

def triangle(x1, y1, x2, y2, x3, y3, color, outline="black"):
    pen.pencolor(outline)
    pen.fillcolor(color)
    go(x1, y1)
    pen.begin_fill()
    pen.goto(x2, y2)
    pen.goto(x3, y3)
    pen.goto(x1, y1)
    pen.end_fill()

def circle(center_x, center_y, r, color, outline=None):
    pen.pencolor(outline if outline else color)
    pen.fillcolor(color)
    go(center_x, center_y - r)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()

# небо
def draw_stars(count):
    colors = ["white", "#fff4b0", "#dbeafe", "#fde68a"]
    for _ in range(count):
        x = random.randint(-490, 490)
        y = random.randint(20, 330)
        size = random.randint(2, 5)
        go(x, y)
        pen.dot(size, random.choice(colors))

def draw_moon(x, y, r):
    circle(x, y, r, "#f5f3ce")
    # небольшая "тень", чтобы получился серп
    circle(x + 12, y + 5, r, "#07111f")

# окна
def draw_windows(x, y, w, h, prob=0.35):
    margin_x = 10
    margin_y = 12
    win_w = 12
    win_h = 18
    gap_x = 8
    gap_y = 10

    cols = int((w - 2 * margin_x + gap_x) // (win_w + gap_x))
    rows = int((h - 2 * margin_y + gap_y) // (win_h + gap_y))

    for row in range(rows):
        for col in range(cols):
            wx = x + margin_x + col * (win_w + gap_x)
            wy = y + margin_y + row * (win_h + gap_y)

            if random.random() < prob:
                color = random.choice(["#ffd966", "#fff2a8", "#ffe599"])
            else:
                color = "#16202f"   # тёмное окно

            rect(wx, wy, win_w, win_h, color, color)

# здания
def building_flat(x, y, w, h):
    color = random.choice(["#0b132b", "#1c2541", "#111827", "#16213e"])
    rect(x, y, w, h, color, "black")
    draw_windows(x, y, w, h, 0.38)

def building_roof(x, y, w, h):
    color = random.choice(["#0f172a", "#1e293b", "#1b263b"])
    body_h = h - 30
    rect(x, y, w, body_h, color, "black")
    triangle(x, y + body_h, x + w / 2, y + h, x + w, y + body_h, color, "black")
    draw_windows(x, y, w, body_h - 8, 0.33)

def building_tower(x, y, w, h):
    color = random.choice(["#0b132b", "#1f2937", "#172033"])
    base_h = int(h * 0.75)
    top_w = int(w * 0.55)
    top_x = x + (w - top_w) / 2
    top_h = h - base_h

    rect(x, y, w, base_h, color, "black")
    rect(top_x, y + base_h, top_w, top_h, color, "black")

    # антенна
    go(x + w / 2, y + h)
    pen.pencolor("#404040")
    pen.pensize(2)
    pen.setheading(90)
    pen.forward(18)
    pen.dot(5, "red")
    pen.pensize(1)

    draw_windows(x, y, w, base_h, 0.36)
    draw_windows(top_x, y + base_h + 6, top_w, top_h - 6, 0.30)

# фон и город
def draw_ground():
    rect(-500, -350, 1000, 60, "#0a0a0a", "#0a0a0a")

def draw_distant_buildings():
    x = -500
    while x < 500:
        w = random.randint(50, 100)
        h = random.randint(70, 160)
        rect(x, -290, w, h, "#09101d", "#09101d")
        x += w + random.randint(2, 10)

def draw_city():
    x = -500
    while x < 500:
        w = random.randint(70, 130)
        h = random.randint(150, 330)

        kind = random.choice([1, 2, 3])
        if kind == 1:
            building_flat(x, -300, w, h)
        elif kind == 2:
            building_roof(x, -300, w, h)
        else:
            building_tower(x, -300, w, h)

        x += w + random.randint(5, 15)

def night_city():
    draw_stars(180)
    draw_moon(320, 220, 45)
    draw_distant_buildings()
    draw_city()
    draw_ground()

screen.tracer(0)
night_city()
screen.update()
screen.exitonclick()