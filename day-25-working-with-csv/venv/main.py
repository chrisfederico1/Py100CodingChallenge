# with open("weather_data.csv", mode="r") as data:
#     print(data.readlines())
# 


# import csv
# 
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperatures = []
#     for row in data:
#         temp = int(row[1])
#         temperatures.append(temp)
#     print(temperatures)


import pandas

data = pandas.read_csv("2018_central_park_census.csv")

# data_dict = data.to_dict()
# # print(data_dict)
# 
# temp_list = data["temp"].to_list()
# 
# # print(data["temp"].mean())
# 
# max_temp = data["temp"].max()
# print(max_temp)
# 

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Get squirrel count
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count")




