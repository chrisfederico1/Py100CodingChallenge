# loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


# Practice student height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for s in student_heights:
    total_height += s 
# print(f"total height = {total_height}")

total_students = 0

for student in student_heights:
  total_students += 1

# print(f"number of students = {total_students}")

average_height = round(total_height / total_students)
print(average_height)


# practice with for loops
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# using loops with the range function 


