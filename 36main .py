# a = input("enter a first number:")
# print(f" Multiplication table of {a} is:")
# try:
#  for i in range(1,11):
#     print(f"{int(a)} x {i}= {int(a)* i}")
# except:
#   print("some Input!")


# print("Some imp  lines of code")
# print("End of program")

try:
    num = int(input("Enter an interger: "))
    a = [6 , 3]
    print(a[num])
except ValueError:
    print("number enterd is not an interger.")
except IndexError:
  print("Index Error")