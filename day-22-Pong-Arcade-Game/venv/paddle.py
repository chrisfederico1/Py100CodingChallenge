from turtle import Turtle
WIDTH = 1000
HEIGHT = 600
Y = 20


class Paddle():

    def __init__(self):
        self.paddle1 = Turtle()
        self.paddle2 = Turtle()
        self.create_paddle1()
        self.create_paddle2()

    def create_paddle1(self):
        self.paddle1.color("white")
        self.paddle1.shape("square")
        self.paddle1.shapesize(stretch_wid=7, stretch_len=1)
        self.paddle1.speed(0)
        self.paddle1.penup()
        self.paddle1.setpos(-WIDTH / 2 + 15, -HEIGHT / 2 + 80)

    def create_paddle2(self):
        self.paddle2.color("white")
        self.paddle2.shape("square")
        self.paddle2.shapesize(stretch_wid=7, stretch_len=1)
        self.paddle2.speed(0)
        self.paddle2.penup()
        self.paddle2.setpos(WIDTH / 2 - 22, HEIGHT / 2 - 75)

    def up_p1(self):
        y = self.paddle1.ycor()
        y += Y
        self.paddle1.sety(y)

    def down_p1(self):
        y = self.paddle1.ycor()
        y -= Y
        self.paddle1.sety(y)

    def up_p2(self):
        y = self.paddle2.ycor()
        y += Y
        self.paddle2.sety(y)


    def down_p2(self):
        y = self.paddle2.ycor()
        y -= Y
        self.paddle2.sety(y)
