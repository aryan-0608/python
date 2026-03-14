class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

aryan = Employee("Aryan", 123)
sachin = programmer("Sachin", 456, "Python")
print(aryan.name)
print(sachin.name)
print(sachin.language)