from heapq import *

def kth_smallest_element_in_a_sorted_matrix(matrix, k):
    min_heap = list()

    for row_number in range(len(matrix)):
        heappush(min_heap, (matrix[row_number][0], matrix[row_number], 0))
    
    smallest_element_count, element = 0, 0
    while min_heap:
        element, row, index = heappop(min_heap)
        smallest_element_count += 1
        if smallest_element_count == k:
            break
        if smallest_element_count < k and len(row) > index + 1:
            heappush(min_heap, (row[index + 1], row, index+ 1))
    
    return element

def main():
    matrix = [
        [2,6,8], 
        [3,7,10],
        [5,8,11]
    ]
    k = 5
    print("Input: matrix = " + str(matrix) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_element_in_a_sorted_matrix(matrix, k))))
    print()

    matrix = [
        [1,5,9],
        [10,11,13],
        [12,13,15]
    ]
    k = 8
    print("Input: matrix = " + str(matrix) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_element_in_a_sorted_matrix(matrix, k))))
    print()

    matrix = [
        [-5]
    ]
    k = 1
    print("Input: matrix = " + str(matrix) + ", k = " + str(k))
    print("Output: " + str((kth_smallest_element_in_a_sorted_matrix(matrix, k))))
    print()

main()