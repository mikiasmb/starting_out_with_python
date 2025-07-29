from turtle import *
x = 200
speed(0)
bgcolor("black")
pencolor("white")
pensize(4)
hideturtle()
penup()
goto(-100, 0)
pendown()
for i in range(8):
    forward(x)
    left(135)
done()
