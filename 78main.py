class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.make_sound()
    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def __init_(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")

d = Dog("Buddy","Labrador")
d.make_sound()

a = Animal("Generic","Unknown")
a.make_sound()

