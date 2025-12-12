## def average(a =1,b=3):
#     print("The average is ", (a+b)/2)
# average(4,6)
# average(b =3)

# average(b=3, a=4)

# def name(fname,mname ="Aryan", lname ="patel"):
#     print("Hello,", fname,mname,lname)

# name("rohan","kumar","sharma")   
# 
def average(*numbers):
    sum = 0
    for  i in numbers:
        sum = sum +i
        #print("Average is :",sum / len(numbers))
        return sum / len(numbers)

c = average(5,6,7,1)
print(c)