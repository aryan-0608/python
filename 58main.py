class person:
    # name ="Aryan"
    # occupation = "Engineer"

    def __init__(self, namename, occupation):
        print("Hey I an a person")
        self.name = namename
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("Aryan", "Engineer")
b = person("Shubham", "Developer")
# print(a.name)

# a.name = "Sachin"
# a.occupation = "Cricketer"
a.info()
b.info()