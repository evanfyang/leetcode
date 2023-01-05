def interval_list_intersections_grokking(first_list, second_list):
    intersections = list()
    i, j, start, end = 0, 0, 0, 1

    while i < len(first_list) and j < len(second_list):
        first_overlaps_second = first_list[i][start] >= second_list[j][start] and first_list[i][start] <= second_list[j][end]

        second_overlaps_first = second_list[j][start] >= first_list[i][start] and second_list[j][start] <= first_list[i][end]

        if first_overlaps_second or second_overlaps_first:
            intersections.append([max(first_list[i][start], second_list[j][start]), min(first_list[i][end], second_list[j][end])])

        if first_list[i][end] < second_list[j][end]: 
            i += 1
        else:
            j += 1

    return intersections

def interval_list_intersection_leetcode(first_list, second_list):
    intersections = list()
    i, j, start, end = 0, 0, 0, 1

    while i < len(first_list) and j < len(second_list):
        low = max(first_list[i][start], second_list[j][start])
        high = min(first_list[i][end], second_list[j][end])

        if low <= high:
            intersections.append([low, high])

        if first_list[i][end] < second_list[j][end]: 
            i += 1
        else:
            j += 1

    return intersections

def interval_list_intersections(first_list, second_list):
    intersections = list()
    i, j, start, end = 0, 0, 0, 1

    while i < len(first_list) and j < len(second_list):
        first_overlaps_second = first_list[i][start] <= second_list[j][end] and first_list[i][end] >= second_list[j][start]

        second_overlaps_first = second_list[j][start] <= first_list[i][end] and second_list[j][end] >= first_list[i][start]

        if first_overlaps_second or second_overlaps_first:
            intersections.append([max(first_list[i][start], second_list[j][start]), min(first_list[i][end], second_list[j][end])])

        if first_list[i][end] < second_list[j][end]: 
            i += 1
        else:
            j += 1

    return intersections

def main():
    first_list = [[1, 3],[5, 6],[7, 9]]
    second_list = [[2, 3],[5, 7]]
    print("Input: first_list = " + str(first_list) + ", second_list = " + str(second_list))
    print("Output: " + str(interval_list_intersections(first_list, second_list)))
    
    first_list = [[1, 3],[5, 7],[9, 12]]
    second_list = [[5, 10]]
    print("Input: first_list = " + str(first_list) + ", second_list = " + str(second_list))
    print("Output: " + str(interval_list_intersections(first_list, second_list)))
    
    first_list = [[0,2],[5,10],[13,23],[24,25]]
    second_list = [[1,5],[8,12],[15,24],[25,26]]
    print("Input: first_list = " + str(first_list) + ", second_list = " + str(second_list))
    print("Output: " + str(interval_list_intersections(first_list, second_list)))

    first_list = [[1,3],[5,9]]
    second_list = []
    print("Input: first_list = " + str(first_list) + ", second_list = " + str(second_list))
    print("Output: " + str(interval_list_intersections(first_list, second_list)))

main()
