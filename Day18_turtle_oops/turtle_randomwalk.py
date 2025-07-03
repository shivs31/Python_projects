import os
os.environ["TK_SILENCE_DEPRECATION"] = '1'
import turtle as t
import random

tim = t.Turtle()
tim.shape("classic")
t.colormode(255) 

#function to select random colors from 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


colors = ["dark green","navy","dark red","purple","deep pink","yellow","teal","royal blue","dark cyan","olive drab","dark orange"]
directions = [0,90,180,270] #from turtle documentation
tim.speed("fastest")
tim.pensize(12)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions)) #select direction angles

screen = t.Screen()
screen.exitonclick()