# with open('file.txt', 'r') as f:
#     print(type(f))          # file object ka type
#     f.seek(10)   
#     print(f.tell())           # file ke 10th byte par move
#     data = f.read(5)        # 5 characters read
#     print(data)


with open('sample.txt', 'w') as f:
    f.write('hello world3!')
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())