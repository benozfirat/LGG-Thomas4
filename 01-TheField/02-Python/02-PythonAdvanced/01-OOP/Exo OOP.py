"""#1 OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicule:
    def __init__(self,max_speed, mileage)
        self.max_speed = max_speed
        self.mileage = mileage

#2 OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicule:
    pass
"""

"""#3 Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

Vehicle Name: School Volvo Speed: 180 Mileage: 12

School_Bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:",School_Bus.name, "Speed:",School_Bus.max_speed, "Mileage:", School_Bus.mileage)

#4 Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
School_Bus = Bus("School Volvo", 180, 12)
print(School_Bus.seating_capacity())
    

#5 Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    colour = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)
print("Colour",School_Bus.colour, "Vehicle name:",School_Bus.name, "Speed:", School_Bus.max_speed, "Mileage:", School_Bus.mileage)
car= Car("Audi Q5", 240, 18)
print(print("Colour",car.colour, "Vehicle name:",car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)) """


"""Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity()
    
    def fare(self):
        return self.capacity * 100 + self.capacity * 10

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

#7 Write a program to determine which class a given Bus object belongs to.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
"""

"""#8 Determine if School_bus is also an instance of the Vehicle class"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))
    
