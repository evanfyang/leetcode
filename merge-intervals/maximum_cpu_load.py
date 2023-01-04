from heapq import *

class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def maximum_cpu_load(jobs):
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []
    
    jobs.sort(key=lambda job: job.start)
    
    for job in jobs:
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            min_heap[0].cpu_load
            heappop(min_heap)

        current_cpu_load += job.cpu_load
        heappush(min_heap, job)
        
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    
    return current_cpu_load

def main():
    jobs = [Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]
    print("Input: " + str(jobs))
    print("Output: " + str(maximum_cpu_load(jobs)))
    
    jobs = [Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]
    print("Input: " + str(jobs))
    print("Output: " + str(maximum_cpu_load(jobs)))

    jobs = [Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]
    print("Input: " + str(jobs))
    print("Output: " + str(maximum_cpu_load(jobs)))

main()
