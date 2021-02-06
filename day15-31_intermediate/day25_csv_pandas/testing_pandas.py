# import csv
# with open ('/Users/brendan/Documents/Python/100daysofcode/day25/data.csv',
#             mode='r') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row [1]!= 'temp':
#             new_temp = int(row[1])
#             temperatures.append(new_temp)

# print(temperatures)

import pandas
data = pandas.read_csv('weather_data.csv')
temp_list = data['temp'].to_list()
# print(temp_list)

# # average_temp = sum(temp_list)/len(temp_list)
# # print(average_temp)
# average_temp = data['temp'].mean()
# max_temp = data['temp'].max()
# print(f'Temperature:\n avg:{round(average_temp)}\n high temp: {max_temp}')

# max_temp = data['temp'].max()
# print(data[data.temp == max_temp])


def convert(temp):
    f = temp * 2 + 30
    return f


print(convert(data[data.day == 'Monday'].temp))
