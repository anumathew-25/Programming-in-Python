import turtle
t=turtle.Turtle()
t.speed(10)

for i in range(5):
    t.circle(190-i,90)
    t.left(90)
    t.circle(190 - i, 90)
    t.left(18)

t.hideturtle()
turtle.done()
