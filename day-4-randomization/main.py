# Random numbers 
# Use Random Module 
import random

random_number = random.randint(1, 10)
# print(random_number)

# You can create separate files you can use as modules

# random number between 0 and 1

random_float = random.random()
print(random_float)

# Print float from 0 - 5 
random_float = random.random() * 5
print(random_float)

# Heads or Tails
coin_result = random.randint(0, 1)

if coin_result == 0:
    print("Tails")
else:
    print("Heads")


# Using lists

# define an index with the []
fruits = ["apples", "Peaches", "Grapes"]
print(fruits[1])


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# find the lenght of the list
lenght = len(names)
#print(lenght)
winner = random.randint(0, lenght - 1)
print(names[winner] + " is going to buy the meal today!")

# Nested lists

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
vertical = int(position[1])
horizontal = int(position[0])

map[vertical - 1] [horizontal - 1] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

