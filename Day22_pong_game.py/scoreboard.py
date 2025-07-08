from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    #Define scoreboard displayed    
    def update_scoreboard(self): 
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    #Tracking left side score
    def l_point(self):
        self.l_score += 1

    #Tracking right side score
    def r_point(self):
        self.r_score += 1