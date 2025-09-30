from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Player A: {self.l_score}", font=("Courier", 18, "normal"))
        self.goto(150, 260)
        self.write(f"Player B: {self.r_score}", font=("Courier", 18, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.update_score()

    def update_r_score(self):
        self.r_score += 1
        self.update_score()

