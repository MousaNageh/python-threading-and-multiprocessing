import multiprocessing
import time 
def proccess1(conn):
    message = conn.recv()
    print(message)
    conn.send("hello process 2 ")
    conn.close()
    return "procees 1 done"

def proccess2(conn):
    conn.send("hello proccess 1")
    message = conn.recv()
    print(message)
    conn.close()
    return "procees 2 done"
conn1, conn2 = multiprocessing.Pipe()

#2 process 
p1 = multiprocessing.Process(target=proccess1, args=(conn1,))
p2 = multiprocessing.Process(target=proccess2, args=(conn2,))
p1.start()
p2.start()




# with process pool 
from concurrent.futures import ProcessPoolExecutor ,as_completed
with ProcessPoolExecutor() as executor:
    future_objs = [executor.submit(proccess1,conn1),executor.submit(proccess2,conn2)] 
    for res in as_completed(future_objs):
        print(res.result())





# for one procese 
p1 = multiprocessing.Process(target=proccess1, args=(conn1,))
p1.start()
# wait conn1 to send value 

conn2.send("hello from main process")
p1_res = conn2.recv()
print(p1_res)
conn2.close()

