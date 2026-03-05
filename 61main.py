class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee is {self.name} and id is {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print("The language is Python")


e1 = Employee("Aryan Patel", 123)
e1.showDetails()

e2 = Programmer("Rohit Patel", 456)
e2.showDetails()
e2.showLanguage()