"""
Access any objects with behaviour / methods without having to inherit the parent class
"""

class Dog:
    def Speak(self):
        print("Lol, Lol")


class Cat:
    def Speak(self):
        print("Meow, Meow")

class AnimalSpeaks:
    def Sound(self, animal):
        animal.Speak()

dog = Dog()
cat = Cat()
animal = AnimalSpeaks()
animal.Sound(dog)
animal.Sound(cat)
