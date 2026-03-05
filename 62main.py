# class Employee:
#     def __init__(self):
#         self.__name = "Aryan Patel"

# a = Employee()
# # print(a.__name) # Cannot be accessed directly

# print(a._Employee__name)  # can be accsed indirectly

# print(a.__dir__())  # shows the name mangled variable


class Student:
    def __init__(self):
        self._name = "John Doe"

        # protected variable
    def _funName(self):
        return "This is a protected method"
        
class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
# calling by object of student class
print(obj._name)
print(obj._funName())

    # calling by object of subject class
print(obj1._name)
print(obj1._funName())
