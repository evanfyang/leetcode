from heapq import * 

def kth_smallest_element(nums, k):
    max_heap = list()
    for i in range(k):
        heappush(max_heap, -nums[i])
    
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
        else:
            continue
    
    return max_heap[0]

def kth_largest_element_in_an_array(nums, k):
    min_heap = list()
    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
        else:
            continue
    
    return min_heap[0]

def main():
    nums = [1,5,12,2,11,5]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(kth_largest_element_in_an_array(nums, k)))
    print()

    nums = [1,5,12,2,11,5]
    k = 4
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(kth_largest_element_in_an_array(nums, k)))
    print()

    nums = [5,12,11,-1,12]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(kth_largest_element_in_an_array(nums, k)))
    print()

    nums = [3,2,1,5,6,4]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(kth_largest_element_in_an_array(nums, k)))
    print()

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(kth_largest_element_in_an_array(nums, k)))
    print()

main()