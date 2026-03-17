import time

# def usingWhile():
#     i = 0
#     while i < 100:
#         i = i + 1
#         print(i)

# def usingFor():
#     for i in range(100):
#         print(i)
# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)


# print(4)
# time.sleep(2)
# print("this is printed after 3 second")

t = time.localtime()
formatted_time = time.strftime("%H:%M:%S", t)
print(formatted_time)