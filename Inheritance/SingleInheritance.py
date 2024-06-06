"""
Child inherits Parent class functionalities
"""
class Vehicle:
    def setTopSpeed(self, speed: int) -> None:
        self.speed = speed
        print("Top Speed: ", self.speed)


class Car(Vehicle):
    def noOfDoors(self, doors: int) -> None:
        self.doors = doors
        print("No of Doors in Car: ", self.doors)
    
car = Car()
car.setTopSpeed(120)
car.noOfDoors(5)
