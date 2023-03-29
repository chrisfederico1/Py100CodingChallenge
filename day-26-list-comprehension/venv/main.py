# List comprehesion formula
import random

# new_list = [new_item for item in list]

# Conditional Comprehesion formula

# new_list = [new_item for item in list if test]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
# 
# #Write your 1 line code 👇 below:
# squared_numbers = [n * n for n in numbers]
# 
# 
# #Write your code 👆 above:
# 
# print(squared_numbers)
# 
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
# 
# #Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
# 
# 
# #Write your code 👆 above:
# 
# print(result)
# 
# new_list1 = []
# new_list2 = []
# with open("file1.txt", mode="r") as f1:
#     for line in f1.readlines():
#         new_list1.append(line.strip())
# 
# with open("file2.txt", mode="r") as f2:
#     for line in f2.readlines():
#         new_list2.append(line.strip())
# 
# 
# result = [int(num) for num in new_list1 if num in new_list2]
# 
# 
# 
# 
# # Write your code above 👆
# 
# print(result)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}


passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(passed_students)
