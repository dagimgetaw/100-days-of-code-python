with open("weather_data.csv", mode="r") as file:
    data = file.readlines()
    print(data)


import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)

import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data), type(data["temp"]))
temp_list = data["temp"].to_list()
print(f"mean of the data is {data['temp'].mean()}")
print(f"max value of the data is {data['temp'].max()}")
print(data[data.day == "Monday"])


max_temp = data["temp"].max()
max_temp_day = data[data["temp"] == max_temp]

max_temp_day2 = data[data.temp == data.temp.max()]
print(max_temp_day2)

