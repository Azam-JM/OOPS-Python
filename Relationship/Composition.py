"""
Part-of relationship - Strong relationship
Owned class objects lifecycle depends on owner class
"""
class Engine:
    def __init__(self, capacity: str) -> None:
        self.capacity = capacity

    def printDetails(self):
        print("Engine type:", self.capacity)

class Tyre:
    def __init__(self, count: int) -> None:
        self.count = count
    
    def printDetails(self):
        print("Tyre count:", self.count)

class Door:
    def __init__(self, doors: int) -> None:
        self.doors = doors
    
    def printDetails(self):
        print("Doors Count:", self.doors)

class Car:
    def __init__(self, engine: str, tyre: int, door: int) -> None:
        self.engineObject = Engine(engine)
        self.tyreObject = Tyre(tyre)
        self.doorObject = Door(door)

    def printDetails(self):
        self.engineObject.printDetails()
        self.tyreObject.printDetails()
        self.doorObject.printDetails()


car = Car("Petrol", 4, 4)
car.printDetails()