from heapq import *

def kth_smallest_number_in_m_sorted_lists(lists, k):
    min_heap = list()
    for list_number in range(len(lists)):
        heappush(min_heap, (lists[list_number][0], list_number, 0))
    
    value = 0
    smallest_number_count = 1
    while min_heap:
        value, list_number, index = heappop(min_heap)
        if smallest_number_count == k:
            break
        elif smallest_number_count < k and len(lists[list_number]) > index + 1:
            heappush(min_heap, (lists[list_number][index + 1], list_number, index + 1))
        smallest_number_count += 1
    
    return value

def main():
    lists = [[2,6,8],[3,6,7],[1,3,4]]
    k = 5
    print("Input: lists = " + str(lists) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_number_in_m_sorted_lists(lists, k))))
    print()

    lists = [[5,8,9],[1,7]]
    k = 3
    print("Input: lists = " + str(lists) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_number_in_m_sorted_lists(lists, k))))
    print()

    lists = [[1,4,5],[1,3,4],[2,6]]
    k = 7
    print("Input: lists = " + str(lists) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_number_in_m_sorted_lists(lists, k))))
    print()

main()