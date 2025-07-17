# with open("/Users/shivani/udemy_ds/python_projects/Day25_US_states_guessinggame/weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

import csv

with open('/Users/shivani/udemy_ds/python_projects/Day25_US_states_guessinggame/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

