from heapq import *

def top_k_elements(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] <= min_heap[0]:
            continue
        else:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    
    return list(min_heap)

def main():
    nums = [3,1,5,12,2,11]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_elements(nums, k)))
    print()

    nums = [5,12,11,-1,12]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_elements(nums, k)))
    print()

main()