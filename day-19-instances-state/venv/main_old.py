from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()


def turn_right():
    tim.rt(5)


def turn_left():
    tim.lt(5)
    

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.bk(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
