def longest_subarray_with_ones_after_replacement(k, nums)    
    windowStart, maxRepeatingOnesCount, maxConsecutiveOnes = 0, 0, 0

    for windowEnd in range(len(nums)):
        if nums[windowEnd] == 1:
            maxRepeatingOnesCount += 1
            
        if ((windowEnd - windowStart + 1) - maxRepeatingOnesCount > k):
            if nums[windowStart] == 1:
                maxRepeatingOnesCount -= 1
            windowStart += 1

        maxConsecutiveOnes = max(maxConsecutiveOnes, windowEnd - windowStart + 1)
        
    return maxConsecutiveOnes

def main():
    k = 2, nums = [1,1,1,0,0,0,1,1,1,1,0]
    print("Input: " + "k = " + k + ", nums = " + nums)    
    print("Output: " + longest_subarray_with_ones_after_replacement(k, nums))
    
    k = 3, nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    print("Input: " + "k = " + k + ", nums = " + nums)    
    print("Output: " + longest_subarray_with_ones_after_replacement(k, nums))

main()
