# # Dictionary. Its basically a hash table
# 
# programming_dictionary = {
#         "Bug": "An error in a program that prevents the program from running as expected.",
#         "Function": "A piece of code that you can easily call over and over again.",
#         "loop": "The action of doing something over and over again.",
# }
# 
# print(programming_dictionary["Bug"])
# 
# # Adding to the dictionary
# programming_dictionary["variable"] = "a character that holds data."
# 
# # print the dictionary
# # print(programming_dictionary)
# 
# # Create an empty dictionary 
# empty_dictionary = {}
# 
# # wipe an existing dictionary
# # programming_dictionary = {}
# 
# # edit an item in a dictionary 
# programming_dictionary["Bug"] = "A moth in your computer."
# 
# # print(programming_dictionary)
# 
# # loop thru a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# Grading program 

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# 
# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# 
# 
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] >= 91 and student_scores[student] <= 100:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] >= 81 and student_scores[student] <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] >= 71 and student_scores[student] <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#     
#     
# 
# # 🚨 Don't change the code below 👇
# print(student_grades)

# nesting dictionaries

capitals = {"France": "Paris",
            "Germany": "Berlin",
            }

# Dictionary in a dictionary

travel_log = {
        "France": {"cites_visited": ["Paris", "Lille", "Dijon"]},
        "Germany": {"german_cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                    "time_spent": 12},
        }

# nesting a dictionary in list


travel_log = [
        {
            "country": "France", 
            "cites_visited": ["Paris", "Lille", "Dijon"],
            "total_visits": 12
        },
        {
            "country": "Germany",
            "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
            "total visits": 5
        },
        ]

# Dictionaries in a list 
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, num_of_visits, cities_visited):
    new_country = {"country": country_visited, "visits": num_of_visits, "cities": cities_visited}
 
    travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



