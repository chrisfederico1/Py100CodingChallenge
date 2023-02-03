#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import System module to clear the screen
from os import system

# Import art
from art import logo

# Import random
import random

# Clear the screen
system('clear')

# Print the logo
print(logo)

WINNING_NUMBER = random.randint(1, 100)


def compare_numbers(guess):
    if guess < WINNING_NUMBER:
        return "Too Low."
    elif guess > WINNING_NUMBER:
        return "Too High."
    else:
        return "You got it!"


# Varible for meessage 
message = "Welcome to the Number Guessing Game!\n\
I'm thinking of a number between 1 and 100."

# create to variables for easy and help
easy = 10
hard = 5


# Print message
print(message)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# if easy then use a for loop of 5 attempts to get the numnber
if difficulty == "hard":
    for i in range(0, 5):
        print(f"You have {hard} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = compare_numbers(guess)
        if result == "Too Low.":
            print(f"{result}\nGuess again.")
            hard -= 1
        elif result == "Too High.":
            print(f"{result}\nGuess again.")
            hard -= 1
        else:
            print(f"{result} The answer was {WINNING_NUMBER}.")
            break
else:
    for i in range(0, 10):
        print(f"You have {easy} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = compare_numbers(guess)
        if result == "Too Low.":
            print(f"{result}\nGuess again.")
            easy -= 1
        elif result == "Too High.":
            print(f"{result}\nGuess again.")
            easy -= 1
        else:
            print(f"{result} The answer was {WINNING_NUMBER}.")
            break
        


print ("You have run out of chances please play again!")

