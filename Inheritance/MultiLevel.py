"""
Child inherits Parent class functionalities and child1 inherits childs functionalities and its parents
"""

class Vehicle:
    def setTopSpeed(self, speed: int) -> None:
        self.speed = speed
        print("Top Speed: ", self.speed)


class Car(Vehicle):
    def noOfDoors(self, doors: int) -> None:
        self.doors = doors
        print("No of Doors in Car: ", self.doors)

class Hybrid(Car):
    def turnOnHybrid(self) -> None:
        print("Hybrid Mode turned ON")


hybrid = Hybrid()
hybrid.setTopSpeed(100)
hybrid.noOfDoors(5)
hybrid.turnOnHybrid()
