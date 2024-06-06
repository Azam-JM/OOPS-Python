from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) -> None:
        pass

    def perimeter(self) -> None:
        pass

class Square(Shape):
    def __init__(self, length) -> None:
        self.length = length

    def area(self) -> None:
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(5)
print(square.area())
print(square.perimeter())
