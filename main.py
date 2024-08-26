import concurrent.futures
import time
import threading

def process_task(task):
    print(f"Processing task {task}")
    time.sleep(2)
    return f"Result of task {task}"

def pooling():
    tasks = [1, 2, 3, 4, 5]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_task, tasks)
        for future_task in results:
            print(f"Task completed with result:{future_task}")

time1 = time.perf_counter()
pooling()
time2 = time.perf_counter()
time11 = time2 - time1
print(time11)