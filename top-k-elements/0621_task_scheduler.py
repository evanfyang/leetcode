from heapq import *

def task_scheduler(tasks, k):
    time_to_finish_tasks = 0
    task_frequency = dict()
    for task in tasks:
        task_frequency[task] = task_frequency.get(task, 0) + 1

    max_heap = list()
    for task, frequency in task_frequency.items():
        heappush(max_heap, (-frequency, task))

    while max_heap:
        waitlist = list()
        # try to execute as many as 'k + 1' tasks from the max_heap
        n = k + 1
        
        while n > 0 and max_heap:
            time_to_finish_tasks += 1
            frequency, task = heappop(max_heap)
            if -frequency > 1:
                # decrement the frequency and add to the waitlist
                waitlist.append((frequency + 1, task))
            n -= 1
        
        # put all the waiting list back on the heap
        for frequency, task in waitlist:
            heappush(max_heap, (frequency, task))
        
        # there will be 'n' idle intervals for the next iteration
        if max_heap:
            time_to_finish_tasks += n
    
    return time_to_finish_tasks

def main():
    tasks = ["A","A","A","B","C","C"]
    k = 2
    print("Input: tasks = " + str(tasks) + ", k = " + str(k))
    print("Output: " + str(task_scheduler(tasks, k)))
    print()

    tasks = ["A","B","A"]
    k = 3
    print("Input: tasks = " + str(tasks) + ", k = " + str(k))
    print("Output: " + str(task_scheduler(tasks, k)))
    print()

    tasks = ["A","A","A","B","B","B"]
    k = 2
    print("Input: tasks = " + str(tasks) + ", k = " + str(k))
    print("Output: " + str(task_scheduler(tasks, k)))
    print()

    tasks = ["A","A","A","B","B","B"]
    k = 0
    print("Input: tasks = " + str(tasks) + ", k = " + str(k))
    print("Output: " + str(task_scheduler(tasks, k)))
    print()

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    k = 2
    print("Input: tasks = " + str(tasks) + ", k = " + str(k))
    print("Output: " + str(task_scheduler(tasks, k)))
    print()

main()