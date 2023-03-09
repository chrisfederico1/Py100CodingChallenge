from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard

# Create Screen object
screen = Screen()
# setup screen width and height
screen.setup(width=1000, height=600)
# setup background color
screen.bgcolor("black")
# setup Title 
screen.title("Pong Game")


paddle = Paddle()
scoreboard = Scoreboard()

# Key Bindings
screen.listen()
screen.onkey(key="w", fun=paddle.up_p1)
screen.onkey(key="s", fun=paddle.down_p1)
screen.onkey(key="Up", fun=paddle.up_p2)
screen.onkey(key="Down", fun=paddle.down_p2)


























screen.exitonclick()
