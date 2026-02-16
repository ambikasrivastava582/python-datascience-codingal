import turtle
t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("lightblue")
t.speed(5)

# ----- Square -----
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("red")
for i in range(4):
    t.forward(100)
    t.right(90)

# ----- Triangle -----
t.penup()
t.goto(0, 100)
t.pendown()
t.color("green")
for i in range(3):
    t.forward(100)
    t.left(120)

# ----- Circle -----
t.penup()
t.goto(200, 100)
t.pendown()
t.color("blue")
t.circle(50)

# ----- Star -----
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("purple")
for i in range(5):
    t.forward(100)
    t.right(144)

# ----- Colorful Pattern -----
t.penup()
t.goto(150, -100)
t.pendown()
colors = ["red","orange","yellow","green","blue","purple"]

for i in range(60):
    t.color(colors[i % 6])
    t.forward(5 * i)
    t.right(59)

turtle.done()
