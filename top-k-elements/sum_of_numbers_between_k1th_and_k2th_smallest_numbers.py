from heapq import * 

def sum_of_numbers_between_k1th_and_k2th_smallest_numbers_min_heap(nums, k1, k2):
    min_heap = list()
    for num in nums:
        heappush(min_heap, num)
    
    for _ in range(k1):
        heappop(min_heap)
    
    sum_between_k1th_and_k2th_smallest_numbers = 0
    for _ in range(k2 - k1 - 1):
        sum_between_k1th_and_k2th_smallest_numbers += heappop(min_heap)

    return sum_between_k1th_and_k2th_smallest_numbers

def sum_of_numbers_between_k1th_and_k2th_smallest_numbers_max_heap(nums, k1, k2):
    max_heap = list()
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    
    sum_between_k1th_and_k2th_smallest_numbers = 0
    for _ in range(k2 - k1 - 1):
        sum_between_k1th_and_k2th_smallest_numbers += -heappop(max_heap)

    return sum_between_k1th_and_k2th_smallest_numbers

def main():
    nums = [1,3,12,5,15,11]
    k1 = 3
    k2 = 6
    print("Input: nums = " + str(nums) + ", k1 = " + str(k1) + ", k2 = " + str(k2))
    print("Output: " + str(sum_of_numbers_between_k1th_and_k2th_smallest_numbers_max_heap(nums, k1, k2)))
    print()

    nums = [3,5,8,7]
    k1 = 1
    k2 = 4
    print("Input: nums = " + str(nums) + ", k1 = " + str(k1) + ", k2 = " + str(k2))
    print("Output: " + str(sum_of_numbers_between_k1th_and_k2th_smallest_numbers_min_heap(nums, k1, k2)))
    print()

main()