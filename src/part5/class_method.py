class Car:
    def __init__(self, body_type):
        self.body_type = body_type

    def __repr__(self):
        return f"Car {self.body_type} body type"

    def set_body_type(self, body_type):
        self.body_type = body_type

    @classmethod
    def hyundai(cls):
        return cls("sedan")

    @classmethod
    def ferrari(cls):
        return cls("convertible")


# c = Car(body_type="sport")
# print(c.body_type)
# c.set_body_type("sedan")
# print(c.body_type)

print(Car.hyundai())
print(Car.ferrari())

# class methods take a cls parameter that points to the class-and not the object instance-when the method is called
# Because the class method has access to this cls argument, it can't modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the cls
