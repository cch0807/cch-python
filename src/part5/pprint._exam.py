# pprint
cars = {
    "tesla": {
        "models": "sedan",
        "model3": "sedan",
        "modelx": "suv",
        "modely": "suv"
    }
}
from pprint import pprint
pprint(cars)
print(cars)

# Walrus Operator
# Available Python 3.8 or later
# a.k.a colon equal operator
# assignment vs. assignment expression

print((walrus := True))

num = [1,2,3,4,5]
description = {
    "length": (num_length := len(num)),
    "sum": (num_sum := sum(num)),
    "mean": num_sum / num_length
}

print(description)
print(num_length)

# ljust & rjust & center
print("|" + "hello world".ljust(30) + "|")
print("|" + "hello world".rjust(30) + "|")
print("|" + "hello world".center(30) + "|")

