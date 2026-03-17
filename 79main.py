class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name of the employee is {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name =name

o = DancerEmployee("Ballet","Aryan")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())