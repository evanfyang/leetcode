from heapq import *

def top_k_frequent_numbers(nums, k):
    num_frequency = dict()
    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1
    
    min_heap = list()
    for num, frequency in num_frequency.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)
    
    top_k_frequent_numbers = list()
    while min_heap:
        top_k_frequent_numbers.append(heappop(min_heap)[1])
    
    return top_k_frequent_numbers

def main():
    nums = [1,3,5,12,11,12,11]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_frequent_numbers(nums, k)))
    print()

    nums = [5,12,11,3,11]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_frequent_numbers(nums, k)))
    print()

    nums = [1,1,1,2,2,3]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_frequent_numbers(nums, k)))
    print()

    nums = [1]
    k = 1
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(top_k_frequent_numbers(nums, k)))
    print()

main()