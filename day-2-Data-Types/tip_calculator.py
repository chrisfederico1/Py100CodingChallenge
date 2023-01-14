# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Start with the greeting
print("Welcome to the tip calculator")
# Get total bill
total = float(input("What is the total bill? "))
# Get what percentage tip would you like to give
tipPercentage = int(input("What percentage of the tip would you like to give? 10, 12, or 15? "))
# Turn percentage in to float number by divifing by 100
tip_to_float = tipPercentage / 100
# multiply it by the total bill and add tip to main bill
final_total = (total * tip_to_float) + total
# Round the final_total with 2 decimal places
# final_total = round(final_total, 2)
print(f'${final_total:.2f}')
people = int(input("How many people should split the bill? "))
pay_per_person = round(final_total / people, 2)

print(f"Each person should pay: ${pay_per_person:.2f}")

