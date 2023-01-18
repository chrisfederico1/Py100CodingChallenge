print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Ask for input at the crossroad notice the single and double quotes
# also notice the \n new line and turn input to lower case
cross_road = input("You're at a crossroad. Where do you want to go? " + '"left "' + "or " + '"right"\n').lower()

if cross_road == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type " + '"wait" ' + "to wait for the boat. Type " + '"swim" ' + "to swim across.\n").lower()
    if lake == "wait":
        island = input("You arrive at the island unharmed. There is a house with 4 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if island == "red":
            print("Burned by fire. Game Over.")
        elif island == "blue":
            print("Eaten by beasts. Game Over.")
        elif island == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by a trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
