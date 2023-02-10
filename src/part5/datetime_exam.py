import datetime

current = datetime.datetime.now()
print(current)

print(current.year)
print(current.month)
print(current.day)
day_of_week = current.weekday()
print(day_of_week)

custom_date = datetime.datetime(year=2022, month=1, day=30)

print(custom_date)

# string to datetime object
datetime_object = datetime.datetime.strptime("2022-01-30 00:00:00", "%Y-%m-%d %H:%M:%S")

print(datetime_object)

# datetime object to string
datetime_str = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
print(type(datetime_str))
print(datetime_str)

# timedelta
from datetime import timedelta

print(datetime_object + timedelta(days=1))
