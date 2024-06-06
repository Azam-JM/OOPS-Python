class Shape:
    def __init__(self) -> None:
        self.sides = 0
    
class Rectangle(Shape):
    def __init__(self, length=0, width=0) -> None:
        self.length = length
        self.width = width
        self.sides = 4
    
    def getArea(self) -> float:
        return (self.length * self.width)
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        self.sides = 0
    
    def getArea(self) -> float:
        return (3.14 * self.radius * self.radius)

shapes = [Rectangle(5,6), Circle(6)]
print(shapes[0].getArea())
print(shapes[1].getArea())
print(shapes[0].sides)
print(shapes[1].sides)