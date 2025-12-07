x = int(input("Enter the value of x:"))
# x is the variable to be checked
match x:
    # if x is 0
    case 0:
        print("x is zero")
        # case with if -condition
    case 4:
        print("x is four")
    case _ if x!=90:
        print("x is not 90 and not in above cases")
    case _ if x!=80:
        print("x is not 80 and not in above cases")
    case _:
        print("x is something else")