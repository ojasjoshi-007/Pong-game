from turtle import Screen, Turtle
import time
from ballclass import Ball
from pong import Paddle
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("orange")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0, 300)
line.setheading(270)
for _ in range(30):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)


screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
ball=Ball()
track=Scoreboard()
game_is_on=True
ball_speed=0.11
while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move_ball()
    if track.l_score >=5:
        ball.hideturtle()
        tim = Turtle()
        tim.pencolor("Black")
        tim.penup()
        tim.hideturtle()
        tim.write("Player A wins",font=18)
        game_is_on=False

    if track.r_score >=5:
        ball.hideturtle()
        tim=Turtle()
        tim.pencolor("Black")
        tim.penup()
        tim.hideturtle()
        tim.write("Player B wins",font=18)
        game_is_on=False

    if ball.ycor()>275 or ball.ycor()<=-275:
        ball.bounce()

    if (330 < ball.xcor() < 350) and (r_paddle.ycor() - 60 < ball.ycor() < r_paddle.ycor() + 60):
        ball.x_bounce()


    if (-350 < ball.xcor() < -330) and (l_paddle.ycor() - 60 < ball.ycor() < l_paddle.ycor() + 60):
        ball.x_bounce()

    if ball.xcor()>380:
       ball.reset_game()
       time.sleep(1)
       ball.x_bounce()
       track.update_l_score()
       ball_speed*=0.85

    if ball.xcor() <-380:
       ball.reset_game()
       time.sleep(1)
       ball.x_bounce()
       track.update_r_score()
       ball_speed*=0.85


screen.exitonclick()
