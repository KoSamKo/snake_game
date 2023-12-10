from turtle import Turtle

FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230,250)
        self.score
        self.upadate_score()

    def upadate_score(self):
        self.write(f"Score: {self.score}", align='center', font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.upadate_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game_Over", align='center', font=FONT)
