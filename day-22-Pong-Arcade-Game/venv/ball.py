from turtle import Turtle
from os import system


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(40)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = -2

    def hit_ball(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def check_top_bottom(self):
        # Top and Bottom Border
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1  # Reverse the direction
            system("aplay bounce.wav&")
        elif self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1
            system("aplay bounce.wav&")
