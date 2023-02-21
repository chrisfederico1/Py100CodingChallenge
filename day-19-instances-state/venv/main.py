
from turtle import Turtle, Screen
import random

# chris = Turtle(shape="turtle")
screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def starting_lineup():
    y = -100
    all_turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for color in colors:
        # create the turtle name based on color
        chris = Turtle(shape="turtle")
        chris.penup()
        chris.color(color)
        chris.goto(x=-230, y=y)
        all_turtles.append(chris)
        y += 40
    return all_turtles


lineup = starting_lineup()

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in lineup:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
