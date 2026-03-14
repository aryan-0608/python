class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

        @classmethod
        def fromstr(cls, string):
            return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Aryan", 1200)
print(e1.name)
print(e1.salary)

string = "John-1200"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def fromstr(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))
    
person = person.fromstr("john Doe, 30")
print(person.name,person.age)

