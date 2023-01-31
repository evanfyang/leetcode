import math
from heapq import *

def smallest_range_covering_elements_from_k_lists(lists):
    min_heap = list()
    range_start, range_end = 0, math.inf
    current_maximum_element = -math.inf

    for array in lists:
        heappush(min_heap, (array[0], array, 0))
        current_maximum_element = max(current_maximum_element, array[0])
    
    while len(min_heap) == len(lists):
        element, array, index = heappop(min_heap)
        
        if range_end - range_start > current_maximum_element - element:
            range_end = current_maximum_element
            range_start = element
        
        if len(array) > index + 1:
            heappush(min_heap, (array[index + 1], array, index + 1))
            current_maximum_element = max(current_maximum_element, array[index + 1])
    
    return [range_start, range_end]

def main():
    lists = [[1,5,8],[4,12],[7,8,10]]
    print("Input: lists = " + str(lists))
    print("Output: " + str((smallest_range_covering_elements_from_k_lists(lists))))
    print()

    lists = [[1,9],[4,12],[7,10,16]]
    print("Input: lists = " + str(lists))
    print("Output: " + str((smallest_range_covering_elements_from_k_lists(lists))))
    print()

    lists = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print("Input: lists = " + str(lists))
    print("Output: " + str((smallest_range_covering_elements_from_k_lists(lists))))
    print()

    lists = [[1,2,3],[1,2,3],[1,2,3]]
    print("Input: lists = " + str(lists))
    print("Output: " + str((smallest_range_covering_elements_from_k_lists(lists))))
    print()

main()