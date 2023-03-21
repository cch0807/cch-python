class Car:
    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")


class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print("No sound ...")


class CombustionEngineCar(Car):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print("vrooom....")


ec = ElectricCar()
ec.start()
ec.drive()

print("------------")

cec1 = CombustionEngineCar()
cec1.start()
cec1.drive()
print(id(cec1))

cec2 = CombustionEngineCar()
print(id(cec2))
