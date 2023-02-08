# import os.System
from os import system

# import Art
from art import logo, vs


# import random
import random

# import game data
from game_data import data

# first clear the screen
system('clear')


def next_time_play(first_pick, second_pick, current_score):
    # Clear screen
    system('clear')

    # get next pick this would be after the user got it right B second pick
    # becomes first pick
    next_pick = getRandom()

    # next print art logo
    print(logo)

    # print your correct with current score
    print(f"You're right! Currect score: {current_score}")
    # print out the first compare
    print(f"Compare A: {second_pick.get('name')}, a {second_pick.get('description')}, from {second_pick.get('country')}.")

    # skip a line
    print("")

    # print vs Art
    print(vs)

    # print Against
    print(f"Against B: {next_pick.get('name')}, a {next_pick.get('description')}, from {next_pick.get('country')}.")

    # Return next_pick
    return next_pick


def first_time_play(first_pick, second_pick):
    # next print art logo
    print(logo)

    # print out the first compare
    print(f"Compare A: {first_pick.get('name')}, a {first_pick.get('description')}, from {first_pick.get('country')}.")

    # skip a line
    print("")

    # print vs Art
    print(vs)

    # print Against
    print(f"Against B: {second_pick.get('name')}, a {second_pick.get('description')}, from {second_pick.get('country')}.")


def compare(first, second):
    # find out who is the winner

    A = first.get('follower_count')
    B = second.get('follower_count')

    if A > B:
        winner = "A"
        return winner
    else:
        winner = "B"
        return winner


def getRandom():
    """
    Function that generates are random pick (dictionary)from the data list
    Returns: pick
    """
    pick = random.choice(data)
    return pick


# get random picks

pick_1 = getRandom()
pick_2 = getRandom()
# if they are the same choose another random
if pick_1 == pick_2:
    pick_2 = getRandom()


# This keeps track of wrong answer
correct_answer = True

# Keep track of current score
current_score = 0

# Call first_time_play

first_time_play(pick_1, pick_2,)

while correct_answer:
    print(pick_1)
    print(pick_2)

    winner = compare(first=pick_1, second=pick_2)

    # ask the user for which has more followers
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == winner:
        current_score += 1
        holder = next_time_play(pick_1, pick_2, current_score)
        pick_1 = holder
        pick_2 = getRandom()
    else:
        print(f"You are wrong. Final Score: {current_score}")
        correct_answer = False
