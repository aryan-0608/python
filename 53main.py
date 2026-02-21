# MAP FUNCTION
# def cube(x):
#     return x*x*x

# print(cube(2))
l=[1,2,3,4,5,6]
# newl=[]
# for iten in l:
#     newl.append(cube(iten))

newl =list(map(lambda x: x*x*x,l))
print(newl)

# FILTER FUNCTION
def filter_function(a):
    return a>0
newnewl =list(filter(filter_function,l))
print(newnewl)

from functools import reduce
numbera1 = [1,2,3,4,5]
numberb2 = [6,7,8,9,10]
def sum(a,b):
    return a+b
sum = reduce(sum,numbera1,numberb2)
print(sum)