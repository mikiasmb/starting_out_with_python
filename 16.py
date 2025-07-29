from turtle import *
f = 5
hideturtle()
bgcolor("black")
pencolor("white")
speed(0)
penup()
goto(150, -150)
pendown()
for i in range(0, 400, 4):
    setheading(90)
    forward(f+i)
    setheading(180)
    forward(f+i)
    setheading(270)
    forward(f+i)
    setheading(0)
    forward(f+i)
done()
