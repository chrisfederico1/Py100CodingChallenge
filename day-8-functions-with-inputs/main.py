# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("hello!")
#     print("How are you ?")
#     print("awesome")
# 
# greet()
# 
# # Function that allows for input 

#  def greet_with_name(name):
#      print(f"Hello {name}")
#      print(f"How do you do {name}?")
#  
#  greet_with_name("Chris")
#  

# function with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")
# 
# # greet_with("heather Locklear", "Nowhere")
# 
# 
# # Call the function with keyword positions
# greet_with(location="riverside", name="laura croft")


# Exercise 

def paint_calc(height, width, cover):
    number_of_cans = round((height * width) / coverage)
    print(f"You'll need {number_of_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# prime numbers

#Write your code below this line 👇

def prime_checker(number):
    # define a flag variable
    flag = False
    if number == 1:
        print("It's not a prime number.")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
            
    if flag:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

    



#Write your code above this 
