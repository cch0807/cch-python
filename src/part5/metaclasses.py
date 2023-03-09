# Metaclasses are just classes that create other classes
# Classes are essentially just building blocks of code that tell
# you how to produce an object. We can then instantiate each object to
# create unique instances of that class.

class Car(object):

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def __repr__(self): # special method
        return f"Brand: {self.brand}, Color: {self.color}"

myTesla = Car("Tesla", "White")
# print(myTesla)
# Brand: Tesla, Color: White
# Python
# instances of the classes is consdered objects, but also class is
# considered object

# myTesla = Car("Tesla", "White")
# # print(type(myTesla))
# # print(type(Car))

# # dynamically created Class
EVCar = type('Car', (), {})
print(EVCar())

'''
Name - Name of the class
Bases - Any classes we inherit from
Attrs - Any Attributes associated with the same class.
type(name, bases, attrs)
'''

# Create Class of Car
class Car(object):

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def __repr__(self):
        return f"Brand: {self.brand}, Color: {self.color}"

# Create additional method for our new Class
def charge(self):
    return "Charging up"