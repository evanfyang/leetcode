from collections import deque

def num_subarrays_product_less_than_k(nums, k):
    window_start, window_product, num_subarrays = 0, 1, 0
    
    if k <= 1:
        return 0

    for window_end in range(len(nums)):
        window_product *= nums[window_end]

        while window_product >= k and window_start <= window_end:
            window_product /= nums[window_start]
            window_start += 1

        num_subarrays += window_end - window_start + 1
    
    return num_subarrays

def subarrays_product_less_than_k(nums, k):
    window_start, window_product = 0, 1
    subarrays = list()

    if k <= 1:
        return []

    for window_end in range(len(nums)):
        window_product *= nums[window_end]

        while window_product >= k and window_start <= window_end:
            window_product /= nums[window_start]
            window_start += 1

        subarray = deque()
        for i in range(window_end, window_start - 1, -1):
            subarray.appendleft(nums[i])
            subarrays.append(list(subarray))
    
    return subarrays

def main():
    nums = [10,5,2,6]
    k = 100
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(num_subarrays_product_less_than_k(nums, k)))

    nums = [1,2,3]
    k = 0
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(num_subarrays_product_less_than_k(nums, k)))

    nums = [2,5,3,10]
    k = 30
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(num_subarrays_product_less_than_k(nums, k)))

    nums = [8,2,6,5]
    k = 50
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(num_subarrays_product_less_than_k(nums, k)))

    nums = [10,5,2,6]
    k = 100
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(subarrays_product_less_than_k(nums, k)))

    nums = [1,2,3]
    k = 0
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(subarrays_product_less_than_k(nums, k)))

    nums = [2,5,3,10]
    k = 30
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(subarrays_product_less_than_k(nums, k)))

    nums = [8,2,6,5]
    k = 50
    print("Input: nums = " + str(nums) + ", k = " +str(k))
    print("Output: " + str(subarrays_product_less_than_k(nums, k)))

main()