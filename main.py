import turtle

wn = turtle.Screen()
wn.setup(width = 650, height = 650)

lollipop = turtle.Turtle()
lollipop.speed(0)
lollipop.hideturtle()
lollipop.fillcolor("pink")

lollipop.penup()
lollipop.goto(0, -100)
lollipop.pendown()
lollipop.begin_fill()
lollipop.circle(100)
lollipop.end_fill()

lollipop.penup()
lollipop.goto(0, 0)
lollipop.pendown()

lollipop.speed(2)

for i in range(47):
    lollipop.forward(1+i/1.1)
    lollipop.left(30-i/12)

lollipop.penup()
lollipop.goto(-10, -100)
lollipop.setheading(270)
lollipop.pendown()

lollipop.forward(150)
lollipop.left(90)
lollipop.forward(10)
lollipop.left(90)
lollipop.forward(150)