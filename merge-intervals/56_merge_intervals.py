def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda interval: interval[0])

    merged_intervals = list()

    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    return merged_intervals

def main():
    intervals = [[1,4],[2,5],[7,9]]
    print("Input: " + str(intervals))
    print("Output: " + str(merge_intervals(intervals)))

    intervals = [[6,7],[2,4],[5,9]]
    print("Input: " + str(intervals))
    print("Output: " + str(merge_intervals(intervals)))

    intervals = [[1,4],[2,6],[3,5]]
    print("Input: " + str(intervals))
    print("Output: " + str(merge_intervals(intervals)))

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Input: " + str(intervals))
    print("Output: " + str(merge_intervals(intervals)))

    intervals = [[1,4],[4,5]]
    print("Input: " + str(intervals))
    print("Output: " + str(merge_intervals(intervals)))

main()
