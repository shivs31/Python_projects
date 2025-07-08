from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT =180


class Snake():

    def __init__(self):
        self.snake_length_add = []
        self.create_snake()
        self.head = self.snake_length_add[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_length(position)

    def add_length(self,position):
        my_snake = Turtle('square')
        my_snake.color('green')
        my_snake.penup()
        my_snake.goto(position) #this position is from for loop i.e., location of snake
        self.snake_length_add.append(my_snake)
    
    def extent(self):
        #add length to snake
        self.add_length(self.snake_length_add[-1].position()) #this position is a method from turtle class
    
    def move(self):
        for snake_len in range(len(self.snake_length_add)-1, 0 ,-1): 
            new_x = self.snake_length_add[snake_len - 1].xcor()
            new_y = self.snake_length_add[snake_len-1].ycor()
            self.snake_length_add[snake_len].goto(new_x, new_y)

        self.snake_length_add[0].forward(MOVE_DISTANCE)

    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
         
    def right(self):
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)
         

         