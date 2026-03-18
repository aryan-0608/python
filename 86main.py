# numbers = [1, 2, 3, 4, 5]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())


# walrus operator

# new to python 3.8
# assignment expression ask walrus operator

# assigns value to varibles as part of larger expression

# happy = False
# print(happy)
# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     foods.append(food)


foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)

