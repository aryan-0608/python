
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning!")
#         fx(*args, **kwargs)
#         print("thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello, World!")

# @greet
# def add(a, b):
#     print(a+b)

# #greet(hello)()  # This will call the decorated function
# hello()
# # /greet(add(2, 3)) This will call the decorated function with arguments
# add(2, 3) 


import logging

def log_function_call(func):
 def decorated(*args, **kwarga):
    logging.info(f"calling {func.__name__} with args: {args} and kwargs: {kwarga}")
    result = func(*args, **kwarga)
    logging.info(f"{func.__name__} returned {result}")
    return result
 return decorated

@log_function_call
def my_function(a,b):
    return a +b

