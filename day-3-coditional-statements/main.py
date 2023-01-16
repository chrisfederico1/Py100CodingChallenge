# Rollercoaster flow chart example
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# 
# # If else example
# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Interactive using the modulo 
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# test to see if the modulo is 0 if it is then number is even if not then else  the number is odd
# result = number % 2
# 
# if result == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
# 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# 
# # If else example
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Leap Year crazy calculation

# 
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# If else example
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age > 45= and age <= 55:
        print ("Mid-life crisis is free")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


    # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# bill = 0
# 
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25    
# if add_pepperoni == "Y":
#     bill += 3
# if extra_cheese == "Y":
#     bill += 1
# 
# print(f"Your final bill is: ${bill}.")


# logical operators and nor and Not 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
