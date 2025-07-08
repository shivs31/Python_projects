from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    #moving ball by 10 pixel
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)
    
    #ball bounce_y 
    def bounce_y(self):
        self.y_move *= -1
    
    #ball bounce_x 
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    #resetting the ball to original position
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()