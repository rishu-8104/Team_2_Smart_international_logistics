# ------------------------------------ UI SETUP --------------------------------------#
from turtle import *

turtle = Turtle()
screen = Screen()
screen.title("3D Cube using Python Turtle")
turtle.color('blue')



# ------------------------------------- CODE -----------------------------------------#

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.goto(50, 50)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.goto(150, 50)
turtle.goto(100, 0)

turtle.goto(100, 100)
turtle.goto(150, 150)

turtle.goto(50, 150)
turtle.goto(0, 100)


screen.mainloop()

