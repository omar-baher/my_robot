import turtle as t

t.penup()
t.speed('fast')
print(f"window width is {t.window_width()}")
print(f'window height is {t.window_height()}')
t.bgcolor('dodger blue')


def draws_rectangle(horizontal: int, vertical: int, color: str):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for x in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)

    t.end_fill()
    t.penup()


def draw_arm(colors: str):
    t.pendown()
    t.begin_fill()
    t.color(colors)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)


def draws_triangle(angle_length: int, color: str):
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.left(60)
    t.forward(angle_length)
    t.right(120)
    t.forward(angle_length)
    t.right(120)
    t.forward(angle_length)
    t.end_fill()
    t.penup()


# feet
t.goto(-100, -150)
draws_rectangle(50, 20, 'blue')
t.goto(-30, -150)
draws_rectangle(50, 20, 'blue')


# legs
t.goto(-25, -50)
draws_rectangle(15, 100, 'grey')
t.goto(-55, -50)
draws_rectangle(-15, 100, 'grey')

# body
t.goto(-90, 100)
draws_rectangle(100, 150, 'red')

# arms
t.goto(-90, 85)
t.setheading(180)
draw_arm('light blue')

t.goto(-90, 20)
t.setheading(180)
draw_arm('purple')

t.goto(10, 85)
t.setheading(0)
draw_arm('goldenrod')

# neck
t.goto(-50, 120,)
draws_rectangle(15, 20, 'grey')

# head
t.goto(-85, 170)
draws_rectangle(80, 50, 'grey')

# eyes
t.goto(-60, 160)
draws_rectangle(30, 10, 'white')
t.goto(-55, 155)
draws_rectangle(5, 5, 'black')
t.goto(-40, 155)
draws_rectangle(5, 5, 'black')

# mouth
t.goto(-65, 135)
draws_rectangle(40, 5, 'black')

# hat
t.goto(-62, 170)
draws_triangle(angle_length=40, color='yellow')
t.hideturtle()

