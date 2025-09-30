from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y_cor = self.ycor() + 30
        self.goto(self.xcor(),new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 30
        self.goto(self.xcor(), new_y_cor)
