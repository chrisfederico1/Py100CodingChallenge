import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color



########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# 
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



def draw_spiralgraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.speed("fastest")
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + 10)


draw_spiralgraph(5)


screen = t.Screen()
screen.exitonclick()

