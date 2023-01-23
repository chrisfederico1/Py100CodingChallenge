# create a flow chart to break down a problem 

# Step 1 Choose a random word from a word list 

# #Step 1 
# import random
# word_list = ["aardvark", "baboon", "camel"]
# 
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# 
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# 
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# 
# chosen_word = random.choice(word_list)
# # print(type(chosen_word))
# 
# 
# # turn the word into a list
# chosen_word = list(chosen_word)
# print(type(chosen_word))
# guess = input("Pick a letter: ").lower()
# 
# for letter in chosen_word:
#     if guess == letter:
#         print("correct")
#     else:
#         print("incorrect")a 



# Step 2 
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# 
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# 
# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# # Empty list
# display = []
# word_lenght = len(chosen_word)
# 
# # add _ to display
# for i in range(word_lenght):
#     display += "_"
# 
# print(display)
# 
# guess = input("Guess a letter: ").lower()
# 
# 
# 
# 
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range(word_lenght):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
#         
# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# 
# print(display)

# Step 3 
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# 
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# 
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# 
# end_of_game = False
# 
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
# 
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
# 
#     print(display)
# 
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
# 
# 


#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])

