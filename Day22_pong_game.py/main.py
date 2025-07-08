from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Pong Game')
screen.tracer(0)

#paddles to hit the ball 

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


#moving the paddle
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect ball collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #ball needs to bounce
        ball.bounce_y()

    #Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
    
    #Detect Right side paddle misses
    if ball.xcor() > 380:
        ball.reset.position()
        scoreboard.l_point()
    
    #Detect left side paddle misses
    if ball.xcor() < -380:
        ball.reset.position()
        scoreboard.r_point()

screen.exitonclick()