from turtle import *
x = 100
hideturtle()
pencolor("white")
penup()
goto(-60, -80)
pendown()
fillcolor("red")
begin_fill()
for i in range(8):
    forward(x)
    left(45)
end_fill()
penup()
goto(-95, -5)
write("STOP", font=("Arial", 50, "normal"))
pendown()
done()
