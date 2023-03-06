from enum import Enum

class Car(Enum):
    HYUNDAI = 1
    KIA = 2
    TESLA = 3
    FORD = 4

print(Car.HYUNDAI)
print(Car.HYUNDAI.name)
print(Car.HYUNDAI.value)

print(type(Car.HYUNDAI))

print(list(Car))
for car in list(Car):
    print(f"{car.name} - {car.value}")

