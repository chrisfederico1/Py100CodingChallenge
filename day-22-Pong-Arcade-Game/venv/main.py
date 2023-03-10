from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

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


paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

# Key Bindings
screen.listen()
screen.onkey(key="w", fun=paddle.up_p1)
screen.onkey(key="s", fun=paddle.down_p1)
screen.onkey(key="Up", fun=paddle.up_p2)
screen.onkey(key="Down", fun=paddle.down_p2)

while True:
    screen.update()

    # Move the ball
    ball.hit_ball()

    # Check Top and Bottom
    ball.check_top_bottom()

    # Check left and right
    if ball.xcor() > 350:
        scoreboard.p1score += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {scoreboard.p1score} Player B: {scoreboard.p2score}", align=ALIGNMENT, font=FONT)
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -350:
        scoreboard.p2score += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {scoreboard.p1score} Player B: {scoreboard.p2score}", align=ALIGNMENT, font=FONT)
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and Ball Collisions
    if ball.xcor() < -340 and ball.ycor() < paddle.paddle1.ycor() + 50 and ball.ycor() > paddle.paddle1.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < paddle.paddle2.ycor() + 50 and ball.ycor() > paddle.paddle2.ycor() - 50:
        ball.dx *= -1



























screen.exitonclick()
