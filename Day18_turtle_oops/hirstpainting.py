# import colorgram

# rgb_colors = []
# colors = colorgram.extract('/Users/shivani/udemy_ds/python_projects/Day18_turtle_oops/image.jpg', 10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.hideturtle()

#Extracted color list from above code.
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = t.Screen()
screen.exitonclick()