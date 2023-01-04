from heapq import *

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end
        
def meeting_rooms_ii(intervals):
    num_meeting_rooms = 0
    min_heap = list()
    
    for interval in intervals:
        while len(minimum_heap) > 0 and interval.start >= min_heap[0].end:
            heappop(min_heap)
        
        heappush(min_heap, interval)
        
        num_meeting_rooms = max(num_meeting_rooms, len(min_heap))
    
    return num_meeting_rooms

def main():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    print("Input: " + str(intervals))
    print("Output: " + str(meeting_rooms_ii(intervals)))
    
    intervals = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    print("Input: " + str(intervals))
    print("Output: " + str(meeting_rooms_ii(intervals)))

    intervals = [Interval(1, 4), Interval(2, 3), Interval(3, 6)]
    print("Input: " + str(intervals))
    print("Output: " + str(meeting_rooms_ii(intervals)))

    intervals = [Interval(4, 5), Interval(2, 3), Interval(2, 4), Interval(3, 5)]
    print("Input: " + str(intervals))
    print("Output: " + str(meeting_rooms_ii(intervals)))

main()
