from turtle import Screen
from paddle import Paddle  
from ball import Ball 
from scoreboard import Scoreboard
import time 

screen = Screen() 
screen.setup(width=800, height= 600)
screen.bgcolor("black") 
screen.title("pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.listen() 
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w") 
screen.onkey(l_paddle.go_down,"s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce_y()


    # detect collision with paddle 
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_x()

    # detect r_paddle missed 
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
    
    #detect l_paddle missed 
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset() 














screen.exitonclick()