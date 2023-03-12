# before Python 3.7
class Car:
    def __init__(self, id, color, brand):
        self.id = id
        self.color = color
        self.brand = brand

car1 = Car(1, 'WHITE', 'TESLA')
print(car1)
# <__main__.Car object at 0x7ff93af45b90>

# problem:
# 1. too many repetition
# 2. need to implement __str__ and __repr__

# As of Python 3.7 and above
import inspect 
from dataclasses import dataclass, astuple, asdict, replace
from pprint import pprint
from typing import List

# frozen: make it immutable
# order: comparing function
# @dataclass
@dataclass(frozen=True, order=True)
class Car:
    id: int
    color: str = ""
    brand: str = ""

# all the functions in the class
pprint(inspect.getmembers(Car, inspect.isfunction))

car1 = Car(1, 'WHITE', 'TESLA')
print(car1)

# you cannot update immutable variable
# car1.id = 5
# print(car1)

car2 = Car(2, 'WHITE', 'TESLA')
print(f'comparing two objects: {car1 < car2}')

# convert to Tuple
print(astuple(car1))

# convert to Dictionary
print(asdict(car1))

# copy the immutable
print(replace(car1, id=3))

@dataclass
class Inventory:
    cars: List[Car]

inventory = Inventory([car1, car2])
print(inventory)

# inheritance
@dataclass(frozen=True)
class Taxi(Car):
    owner_company: str = ""

taxi1 = Taxi(1, "YELLOW", "HYUNDAI", "xyz")

print(taxi1)