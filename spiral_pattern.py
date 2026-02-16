import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(100):
    t.forward(i * 5)
    t.left(90)

turtle.done()
