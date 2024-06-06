"""
HAS-A relationship - Weak relationship
Owned class objects does not depend on the lifecycle on owner class
"""

class Country:
    def __init__(self, name, population) -> None:
        self.name = name
        self.population = population
    
    def printDetails(self) -> None:
        print("Country Name: ", self.name)
        print("Country population: ", self.population)
    
class People:
    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country

    def printDetails(self) -> None:
        print("Person name: ", self.name)
        self.country.printDetails()

# Owning class
country = Country("India", "100 Million")
country.printDetails()

# Owner class
people = People("Maxa", country)
people.printDetails()
