import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)

colors = ["dark green","navy","dark red","purple","deep pink","yellow","teal","royal blue","dark cyan","olive drab","dark orange"]

def draw_shape(num_sides):
    angle = 360/num_sides # angle to draw shapes
    for _ in range(num_sides): 
        tim.forward(100)
        tim.right(angle)
      

for shape_side_n in range(3,11): #starts with 3 sides i.e, triangle until 11 sides
    tim.color(random.choice(colors)) #selects random color from list
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()

