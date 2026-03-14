# dir method

# x = [12,3,4]
# print(dir(x))
# print(x.__add__)

class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        self._private = "This is a private variable"

e1 = Employee("Aryan", 1200)
print(e1.__dict__)

print(help(Employee))