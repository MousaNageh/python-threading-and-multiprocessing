import multiprocessing
import time 


start = time.perf_counter()

def sleep_fun(task_num):
    print(f"task number {task_num} : is start sleeping")
    time.sleep(1)
    print(f"task number {task_num} : finished")




tasks = []
for i in range(20):
    p = multiprocessing.Process(target=sleep_fun,args=[i+1])
    p.start()
    tasks.append(p)

for p in tasks:
    p.join()    


end  = time.perf_counter()
print("total time : ",round(end- start,2)," seconds")

