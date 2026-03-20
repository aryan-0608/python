import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(second):
    print(f"Sleeping for {second} seconds")
    time.sleep(second)
    return second


# 1️⃣ Normal execution
start = time.perf_counter()

func(1)
func(2)
func(3)

end = time.perf_counter()
print(f"Normal time: {end - start} seconds")


# 2️⃣ Thread execution
start = time.perf_counter()

t1 = threading.Thread(target=func, args=(1,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print(f"Thread time: {end - start} seconds")


# 3️⃣ ThreadPool execution
start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(func, [1, 2, 3])

end = time.perf_counter()
print(f"ThreadPool time: {end - start} seconds")