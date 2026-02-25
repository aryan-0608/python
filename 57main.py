class person:
    name = "Aryan"
    occupation = "Student"
    network = "Instagram"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = person()
b = person()
c = person()

a.name = "Shubham"
a.occupation = "Developer"

b.name = "Rohan"
b.occupation = "Designer"
# print(a.name, a.occupation)
a.info()
b.info()

c.info()