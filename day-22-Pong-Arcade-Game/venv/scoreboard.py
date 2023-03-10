from turtle import Turtle
from ball import Ball
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 150)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
