import random
class Cities:
    def __init__(self, name, initial, population, country, area):
        self.name = name
        self.initial = initial
        self.population = population
        self.country = country
        self.area = area
    def getPopulationdensity(self):
        self.Density = self.population/self.area
        return "The Population density of {}, is {} people per km^2".format (self.name, self.Density)

foo1 = Cities("Calgary", "CA", 1500000.00, "Canada", 825)
foo2 = Cities("Edmonton", "ED", 1000000.00, "Candaa", 684)



print("Format order = Name/Initial/Population/Country/Area")
print("{}/{}/{}/{}".format(foo1.name, foo1.initial, foo1.population, foo1.country, foo1.area))

print("{}/{}/{}/{}".format(foo2.name, foo2.initial, foo2.population, foo2.country, foo2.area))

print(foo1.getPopulationdensity())
