class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"The name of the animal is {self.name} and it is a {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    def show_details(self):
        Animal.show_details(self) 
        print(f"The breed of the dog is {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"The color of the golden retriever is {self.color}")

o = GoldenRetriever("Buddy","Golden")
o.show_details()
print(GoldenRetriever.mro())
