class Employee:
    companyName = "Google"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
 
    def showDatails(self):
        print(f"The name of the Employee is {self.name} the raise an amount  in {self.companyName}is{self.raise_amount}")
# Employee.showDatails(emp1)
emp1 = Employee("Aryan Patel")
emp1.raise_amount = 0.03
emp1.companyName = "Google indian"
emp1.showDatails()
emp2 = Employee("John Doe")
emp2.showDatails()