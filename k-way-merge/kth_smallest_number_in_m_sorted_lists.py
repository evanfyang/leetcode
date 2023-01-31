from heapq import *

def kth_smallest_number_in_m_sorted_lists(lists, k):
    min_heap = list()

    # put the 1st element of each list in the min heap
    for list_number in range(len(lists)):
        heappush(min_heap, (lists[list_number][0], lists[list_number], 0))
    
    # take the smallest(top) element form the min heap; if the running count 
    # is equal to k, return the number
    number, smallest_number_count = 0, 0
    while min_heap:
        number, array, index = heappop(min_heap)
        smallest_number_count += 1
        if smallest_number_count == k:
            break
        # if the array of the top element has more elements, add the next element to the heap
        if smallest_number_count < k and len(array) > index + 1:
            heappush(min_heap, (array[index + 1], array, index + 1))
    
    return number

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