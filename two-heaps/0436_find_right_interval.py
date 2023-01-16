from heapq import *

def find_right_interval(intervals):
    max_start_heap = list()
    max_end_heap = list()

    for index in range(len(intervals)):
        heappush(max_start_heap, (-intervals[index][0], index))
        heappush(max_end_heap, (-intervals[index][1], index))
    
    intervals_length = len(intervals)
    # initialize to -1 in case there is no right interval found for a particular 
    # index of intervals
    right_intervals = [-1 for i in range(intervals_length)]

    for _ in range(intervals_length):
        top_end, end_index = heappop(max_end_heap)

        if max_start_heap and -top_end <= -max_start_heap[0][0]:
            top_start, start_index = heappop(max_start_heap)
            
            while max_start_heap and -top_end <= -max_start_heap[0][0]:
                top_start, start_index = heappop(max_start_heap)
            
            right_intervals[end_index] = start_index
            # put the interval back as it could be the next interval of other intervals;
            # we only need to put the most recently popped tuple from the max_start_heap
            # back because we know that all the top_starts from all the previously popped 
            # max_start_heap tuples are only greater than and closest to or equal to the 
            # previous top_end 
            heappush(max_start_heap, (top_start, start_index))
    
    return right_intervals

def main():
    intervals = [[1,2]]
    print("Input: intervals = " + str(intervals))
    print("Output: " + str(find_right_interval(intervals)))

    intervals = [[3,4],[2,3],[1,2]]
    print("Input: intervals = " + str(intervals))
    print("Output: " + str(find_right_interval(intervals)))

    intervals = [[1,4],[2,3],[3,4]]
    print("Input: intervals = " + str(intervals))
    print("Output: " + str(find_right_interval(intervals)))  
  
    intervals = [[2,3],[3,4],[5,6]]
    print("Input: intervals = " + str(intervals))
    print("Output: " + str(find_right_interval(intervals)))  
  
    intervals = [[3,4],[1,5],[4,6]]
    print("Input: intervals = " + str(intervals))
    print("Output: " + str(find_right_interval(intervals)))

main()