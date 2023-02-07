# using file
file = open("README.txt", "r")
print(file.read())
file.close()

# using csv package
import csv

with open("sample.csv", "r") as data_file:
    sample_data = csv.reader(data_file)
    for row in sample_data:
        print(row)

# using pandas
import pandas as pd

data = pd.read_csv("sample.csv")
print(data)

# print(data['number'])