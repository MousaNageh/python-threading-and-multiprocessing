import time 
import threading 


start = time.perf_counter()

def sleep_fun(task_num):
    print(f"task number {task_num} : is start sleeping")
    time.sleep(1)
    print(f"task number {task_num} : finished")




tasks = []
for i in range(20):
    t1 = threading.Thread(target=sleep_fun,args=[i+1])
    t1.start()
    tasks.append(t1)

for t in tasks:
    t.join()    


end  = time.perf_counter()
print("total time : ",round(end- start,2)," seconds")

