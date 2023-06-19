import turtle
import math
x=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("yellow")
x.forward(100)
x.left(90)
x.forward(100)
x.left(135)
side=math.sqrt(100**2+100**2)
x.forward(side)
turtle.done()