import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()




screen = Screen()
screen.exitonclick()