"""
Multiple child inherits from single parent class
"""
class Vehicle: 
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


corolla = Car() 
corolla.setTopSpeed(220) 

volvo = Truck() 
volvo.setTopSpeed(180)