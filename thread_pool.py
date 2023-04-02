from concurrent.futures import ThreadPoolExecutor , as_completed  
import time 
start = time.perf_counter()

def sleep_fun(task_num):
    print(f"task number {task_num} : is start sleeping")
    time.sleep(task_num)
    return (f"task number {task_num} : finished")

with ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    results = [executor.submit(sleep_fun,sec) for sec in seconds]
    for res in as_completed(results):
        print(res.result())
    #this code equal to  , but the results will got after all sleep_fun function call  finished
    results = executor.map(sleep_fun,seconds)
    for res in results:
        print(res)

end  = time.perf_counter()
print("total time : ",round(end- start,2)," seconds")
