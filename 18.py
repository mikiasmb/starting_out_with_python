from turtle import *
x = 4
bgcolor("black")
pencolor("white")
pensize(4)
hideturtle()
speed(0)
penup()
goto(0, 0)
pendown()
for i in range(45):
    x += 4
    left(90)
    forward(x)
done()
