from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect successful crossing(turtle reaches the other side)
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
    





screen.exitonclick()