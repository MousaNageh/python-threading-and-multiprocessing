from concurrent.futures import ProcessPoolExecutor ,as_completed
import time 


start = time.perf_counter()

def sleep_fun(task_num):
    print(f"task number {task_num} : is start sleeping")
    time.sleep(task_num)
    return (f"task number {task_num} : finished")

with ProcessPoolExecutor() as executor:
    #one time method execution 
    future_obj = executor.submit(sleep_fun,1)
    print(future_obj.result())
    # multi time method execution 
    future_objs = [executor.submit(sleep_fun,i) for i in range(2,10)]
    for res in as_completed(future_objs):
        print(res.result())
    # multi time method execution with map 
    future_objs_form_map = executor.map(sleep_fun,[1,2,3,4,5])
    for res in future_objs_form_map:
        print("map ..: ",res)






end  = time.perf_counter()
print("total time : ",round(end- start,2)," seconds")