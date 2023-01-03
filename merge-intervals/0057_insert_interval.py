def insert_interval(intervals, new_interval):
    merged_intervals = list()
    index, start, end = 0, 0, 1

    while index < len(intervals) and intervals[index][end] < new_interval[start]:
        merged_intervals.append(intervals[index])
        index += 1

    while index < len(intervals) and intervals[index][start] <= new_interval[end]:
        new_interval[start] = min(intervals[index][start], new_interval[start])
        new_interval[end] = max(intervals[index][end], new_interval[end])
        index += 1

    merged_intervals.append(new_interval)

    while index < len(intervals):
        merged_intervals.append(intervals[index])
        index += 1    

    return merged_intervals

def main():
    intervals = [[1,3],[5,7],[8,12]]
    new_interval = [4,6]
    print("Input: intervals = " + str(intervals) + ", new_interval = " + str(new_interval))
    print("Output: " + str(insert_interval(intervals, new_interval)))

    intervals = [[1,3],[5,7],[8,12]]
    new_interval = [4,10]
    print("Input: intervals = " + str(intervals) + ", new_interval = " + str(new_interval))
    print("Output: " + str(insert_interval(intervals, new_interval)))
    
    intervals = [[2,3],[5,7]]
    new_interval = [1,4]
    print("Input: intervals = " + str(intervals) + ", new_interval = " + str(new_interval))
    print("Output: " + str(insert_interval(intervals, new_interval)))
    
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print("Input: intervals = " + str(intervals) + ", new_interval = " + str(new_interval))
    print("Output: " + str(insert_interval(intervals, new_interval)))
    
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print("Input: intervals = " + str(intervals) + ", new_interval = " + str(new_interval))
    print("Output: " + str(insert_interval(intervals, new_interval)))

main()
