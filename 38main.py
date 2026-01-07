a = int(input("Enter any value between 5 and 9:"))

if(a<5 or a>9):
    raise ValueError("Value is not in the range of 5 to 9")