def func():
 try:
    l=[1, 2, 3]
    i= int(input("Enter index: "))
    print(l[i])
    return 1
 except :
    print("Index out of range")
    return 0

 finally:
    print("Execution completed")

print("I am always executed")

x = func()
print(x)