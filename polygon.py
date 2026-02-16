import turtle

t = turtle.Turtle()

sides = 7
length = 100
angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()


