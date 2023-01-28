from heapq import *

def least_number_of_unique_elements_after_k_removals(nums, k):
    number_frequency = dict()
    for number in nums:
        number_frequency[number] = number_frequency.get(number, 0) + 1
    
    min_heap = list()
    for number, frequency in number_frequency.items():
        heappush(min_heap, (frequency, number))
    
    while k > 0 and min_heap:
        frequency, number = heappop(min_heap)
        k -= frequency
    
    return len(min_heap) + 1 if k < 0 else len(min_heap)

def maximum_number_of_unique_elements_after_k_removals(nums, k):
    unique_elements_count = 0
    if len(nums) <= k:
        return unique_elements_count

    # find the frequency of each number
    number_frequency = {}
    for number in nums:
        number_frequency[number] = number_frequency.get(number, 0) + 1

    min_heap = []
    # insert all numbers with frequency greater than '1' into the min-heap
    for number, frequency in number_frequency.items():
        if frequency == 1:
            unique_elements_count += 1
        else:
            heappush(min_heap, (frequency, number))

    # following a greedy approach, try removing the least frequent numbers first from 
    # the min-heap
    while k > 0 and min_heap:
        frequency, number = heappop(min_heap)
        # to make an element distinct, we need to remove all of its occurrences except one
        k -= frequency - 1
        if k >= 0:
            unique_elements_count += 1

    # if k > 0, this means we have to remove some distinct numbers
    if k > 0:
        unique_elements_count -= k

    return unique_elements_count

def main():
    print("least number of unique elements after k removals")
    print()

    nums = [5,5,4]
    k = 1
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(least_number_of_unique_elements_after_k_removals(nums, k)))
    print() 

    nums = [4,3,1,1,3,3,2]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(least_number_of_unique_elements_after_k_removals(nums, k)))
    print() 

    print("maximum number of unique elements after k removals")
    print()

    nums = [7,3,5,8,5,3,3]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(least_number_of_unique_elements_after_k_removals(nums, k)))
    print() 

    nums = [3,5,12,11,12]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(least_number_of_unique_elements_after_k_removals(nums, k)))
    print() 

    nums = [1,2,3,3,3,3,4,4,5,5,5]
    k = 2
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(least_number_of_unique_elements_after_k_removals(nums, k)))
    print() 

main()