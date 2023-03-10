from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


# Create Screen object
screen = Screen()
# setup screen width and height
screen.setup(width=800, height=600)
# setup background color
screen.bgcolor("black")
# setup Title
screen.title("Pong Game")
screen.tracer(0)


scoreboard = Scoreboard()
ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Key Bindings
screen.listen()
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")


game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Move the ball
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 

    # Detect Collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
