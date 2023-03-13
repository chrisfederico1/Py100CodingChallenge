 # import turtle graphics
import turtle as t
import random

chris = t.Turtle()

# change colormode
t.colormode(255)

# radius = 20
r = 20

# set turtle Y coordinate
chris.penup()
chris.hideturtle()
chris.sety(-150)


# forward 50 paces
forward = 50

position = 0


color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]


def draw_row():
    # create a for loop 1 to 100
    for i in range(0, 9):
        # create a random color
        random_color = random.choice(color_list)
        chris.dot(r, random_color)
        chris.penup()
        chris.forward(forward)
    chris.dot(r, random_color)


for i in range(0, 5):
    draw_row()
    chris.left(90)
    chris.forward(forward)
    chris.left(90)
    draw_row()
    chris.right(90)
    chris.forward(forward)
    chris.right(90)









screen = t.Screen()
# screen.setup(width=200, height=200)
screen.exitonclick()

