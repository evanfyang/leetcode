def minimum_size_subarray_with_greater_sum(target, nums):
    windowStart, windowSum, minLength = 0, 0, 0
    
    for windowEnd in range(length(nums)):
        windowSum += nums[windowEnd]
        while windowSum > target:
            minLength = min(minLength, windowEnd + 1 - windowStart)
            windowSum -= nums[windowStart]
            windowStart += 1
    
    return minLength

def main():
    target = 7, nums = [2,3,1,2,4,3]
    print(minimum_size_subarray_with_greater_sum(target, nums))

main()
