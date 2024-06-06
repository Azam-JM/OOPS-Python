class Com:
    def __init__(self, real=0, imag=0) -> None:
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp
    
obj1 = Com(5,6)
obj2 = Com(6,7)

obj3 = obj2 + obj1
print(obj3.real)
print(obj3.imag)