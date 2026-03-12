class Employee:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    def changecompany(cls ,  newcompany):
        cls.company = newcompany

e1 = Employee()
e1.name = "Aryan Patel"
e1.show()
e1.changecompany("Google Indian")
e1.show()