# This is the base class we are starting with.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# DONE: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
        
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=4):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def __str__(self):
        return "This bus has a max speed of {speed:.0f}, {miles:.0f} mileage, and a seating capacity of {seats:.0f}.".format(speed=self.max_speed, miles=self.mileage, seats=self.seating_capacity)

    def set_seating_capacity(self, num):
        self.seating_capacity = num

# DONE: Instantiate your Bus class to an object to a variable called school_bus, the max speed 80, and mileage 45000.

school_bus = Bus(80, 45000)
school_bus.set_seating_capacity(42)
print(school_bus)

# DONE: Add seating_capacity as a parameter in the def __init__(), but give it a default property of 4 seating_capacity=4 and add self.seating_capacity = seating_capacity.

# DONE: Create a method in your Bus class called set_seating_capacity, which takes the parameter: seating_capacity and sets self.seating_capacity to equal the seating_capacity parameter.

# DONE: call school_bus.set_seating_capacity and pass a value of 42.

# DONE: Override the __str__ function in the Bus class to print all of the properties onto a single line.

# DONE: Create a new class which will also inherit the Vehicle class (a different type of vehicle than a bus). Inherit everything from vehicle and add one more set_xxxx method to set a property of that vehicle. 

class Car(Vehicle):
    def __init__(self, max_speed, mileage, model="Volvo"):
        super().__init__(max_speed, mileage)
        self.model = model

    def __str__(self):
        return "This car is a {model}, with a max speed of {speed:.0f} and {miles:.0f} miles!".format(model=self.model,speed=self.max_speed,miles=self.mileage)
    
    def set_model(self, model):
        self.model = model

car = Car(214, 3123)
print(car)
car.set_model("BMW")
print(car)

# TODO: Push both new files to your remote Engr102 repository and copy and paste your repository URL as a submission.