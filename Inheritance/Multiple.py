"""
Single child inherits from two parent class
"""

class CombustionCar:
    def setEngineCapacity(self, enginecapacity: int) -> None:
        self.enginecapacity = enginecapacity

    def noOfDoors(self) -> None:
        print("No of Doors: 5")

class ElectricCar:
    def setBatteryCapacity(self, batterCapacity: int) -> None:
        self.batterCapacity = batterCapacity
    
    def noOfDoors(self) -> None:
        print("No of Doors: 4")

class HybridCar(ElectricCar, CombustionCar):
    def printCapacities(self) -> None:
        print("Engine Capacity: ", self.enginecapacity)
        print("Battery Capacity: ", self.batterCapacity)

hybridCar = HybridCar()
hybridCar.setEngineCapacity(40)
hybridCar.setBatteryCapacity(12000)
hybridCar.printCapacities()
hybridCar.noOfDoors()
        