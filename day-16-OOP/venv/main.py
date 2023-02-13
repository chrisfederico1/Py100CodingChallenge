# import turtle graphics
# from turtle import Turtle, Screen
# 
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
# timmy.speed('slowest')
# 
# 
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# create object from the pretty table class
table = PrettyTable()

# Change alignment of table
# table.align = "l"
# add columns to table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)




