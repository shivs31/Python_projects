import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()