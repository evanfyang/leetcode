def longest_subarray_with_ones_after_replacement(nums, k):    
    window_start, max_repeating_ones_count, max_consecutive_ones = 0, 0, 0

    for window_end in range(len(nums)):
        if nums[window_end] == 1:
            max_repeating_ones_count += 1
            
        if ((window_end - window_start + 1) - max_repeating_ones_count > k):
            if nums[window_start] == 1:
                max_repeating_ones_count -= 1
            window_start += 1

        max_consecutive_ones = max(max_consecutive_ones, window_end - window_start + 1)
        
    return max_consecutive_ones

def main():
    k = 2
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    print("Input: " + "k = " + k + ", nums = " + nums)    
    print("Output: " + longest_subarray_with_ones_after_replacement(nums, k))
    
    k = 3
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    print("Input: " + "k = " + k + ", nums = " + nums)    
    print("Output: " + longest_subarray_with_ones_after_replacement(nums, k))

main()
