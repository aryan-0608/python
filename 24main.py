tup =(1 , 2,76,342, "Aryan", True)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("Yes 342 is present in the tuple")
    tup2 = tup[0:4]
    print(tup2)
