from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor 
import math
import time
import os  
import threading 

def cal(c):
    for i in range(1000000):
        math.sqrt(i)

arr = []
for i in range(os.cpu_count()+10):
    arr.append(i)

start  = time.perf_counter()

# threads 
with ThreadPoolExecutor() as executor:
    results = executor.map(cal,arr)

end = time.perf_counter()
print("thread total time : ",round(end- start,2)," seconds")

#proccesses
start  = time.perf_counter()
with ProcessPoolExecutor() as executor:
    results = executor.map(cal,arr)

end = time.perf_counter()
print("process total time : ",round(end- start,2)," seconds")

#threads with in proceesses 
def cal2(c):
    t = threading.Thread(target=cal,args=[c]) 
    t.start()
    t.join()

start  = time.perf_counter()
with ProcessPoolExecutor() as executor:
    results = executor.map(cal2,arr)

end = time.perf_counter()
print("process with thread  total time : ",round(end- start,2)," seconds")