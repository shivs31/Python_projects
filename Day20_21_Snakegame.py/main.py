from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard =Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for length in snake.snake_length_add[1:]:
        #if head collides with any part of the snake body
        #trigger game_over
        if snake.head.distance(length) < 10:
            game_is_on = False
            scoreboard.game_over()
     

screen.exitonclick()