from turtle import Turtle,Screen
screen=Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        screen.setup(width=800,height=600)
        self.speed(1)
        self.shape("circle")
        self.shapesize(stretch_wid=1.5,stretch_len=1.5)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmove=15
        self.ymove=15
    def move_ball(self):
         xcor=self.xcor()+self.xmove
         ycor=self.ycor()+self.ymove
         self.goto(xcor,ycor)
    def bounce(self):
        self.ymove=self.ymove*-1
    def x_bounce(self):
        self.xmove *=-1
    def reset_game(self):
        self.goto(0,0)







