from ball import Ball
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.penup()
        self.p1score = 0
        self.p2score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"Player A: {self.p1score} Player B: {self.p2score}", align=ALIGNMENT, font=FONT)
