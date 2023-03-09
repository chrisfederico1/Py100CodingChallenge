
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Left_Player : {self.score}    Right_Player : {self.score}", align=ALIGNMENT, font=FONT)
