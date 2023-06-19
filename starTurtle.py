import turtle
star=turtle.Turtle()
for i in range(5):
    star.shapesize(1,1,1)
    star.pensize(5)
    star.color("red")
    star.fillcolor("yellow")
    star.begin_fill()
    star.forward(100)
    star.left(144)
    star.end_fill()
turtle.done()    