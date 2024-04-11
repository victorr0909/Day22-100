# import csv
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature =[]
#     for row in data:
#         if row[1]!= "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
            
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)