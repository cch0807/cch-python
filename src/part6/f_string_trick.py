a = 10
b = 20

print(f"{a = }, {b = }")

num = 100

# decimal places
print(f"num: {num:.2f}")

# hex
print(f"hex: {num:#0x}")

# binary
print(f"binary: {num:b}")

# octal
print(f"octal: {num:o}")

# scientific
print(f"scientific: {num:e}")

# add padding
print(f"Number: {num:09}")

# comma separator
num = 100000
print(f"{num = :,}")

# percentage
percentage = 0.97444
print(f"{percentage = :.2%}")

###

import datetime
today = datetime.datetime.now()
# today = datetime.datetime.utcnow()
print(f"current : {today}")
print(f"current : {today:%m/%d/%Y %H:%M:%S}")

###

from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str

    def __str__(self) -> str:
        return f"{self.brand} has {self.model}"
    
model3 = Car("Tesla", "Model 3")
print(f"{model3}") # str

print(f"{model3!r}")

###

text = "Hello World"
num = 50
print(f"{text :>{num}}")
print(f"{text :^{num}}")
print(f"{text :<{num}}")

###

country = "South Korea"
capital = "Seoul"
print(f"""
Country: {country :^30}
Capital: {capital :^30}
""")
