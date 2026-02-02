# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"the local x is {x}")
#     print("hello aryan")

# print(f"the global x is {x}")
# hello()
# x = 5
# print(f"the global x is {x}")

x = 10  # global varible

def my_function():
    global x
    x = 4
    y = 5  # local varible
    print(y)
my_function()
print(x)   # this will cause an error decause y is a local varible and is not accessible outside of the function
# print(y) 