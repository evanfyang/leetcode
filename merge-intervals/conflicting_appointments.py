def conflicting_appointments(intervals):
    start, end = 0, 0    

    intervals.sort(key=lambda interval: interval[start])
    
    for index in range(1, len(intervals)):
        if intervals[index][start] < intervals[index - 1][end]:
            return False
    
    return True

def main():
    intervals = [[1,4],[2,5],[7,9]]
    print("Input: " + str(intervals))
    print("Output: " + str(conflicting_appointments(intervals)))
    
    intervals = [[6,7],[2,4],[8,12]]
    print("Input: " + str(intervals))
    print("Output: " + str(conflicting_appointments(intervals)))

    intervals = [[4,5],[2,3],[3,6]]
    print("Input: " + str(intervals))
    print("Output: " + str(conflicting_appointments(intervals)))

main()
