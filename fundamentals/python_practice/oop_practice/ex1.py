class Vehicle():
    color = "White" #CLASS VARIABLE.  All children will inherit
    

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def __repr__(self): #PRINTS OBJECTS AS READABLE
        return f"Name: {self.name} Speed: {self.max_speed}  Mileage: {self.mileage} Color: {Vehicle.color}"

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100




class Bus(Vehicle): #CHILDREN MUST PASS IN PARENT AS PARAM TO INHERIT


    def seating_capacity(self, capacity=50):
        pass

    def fare(self):
        amount = super().fare()
        amount += amount * .10
        return  amount

class Car(Vehicle):
    pass



school_bus = Bus("School Bus", 65, 42098, 50)
toyota_rav4 = Car("Toyota Rav-4", 150, 14667)

print(school_bus) # Will print 65. (school_bus INSTANCE.max_speed ATTRIBUTE) 
# print(school_bus.seating_capacity())  #INSTANCE.METHOD
# print(repr(school_bus))
# print(repr(toyota_rav4))
# print(f"Total Bus fare is: {school_bus.fare()}")