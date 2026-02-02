# Reading a file
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()


# writing to a file
f = open('myfile.txt', 'a')
f.write('hello world !')
f.close()

with open('myfile.txt','a') as f:
    f.write("hey I am inside with")