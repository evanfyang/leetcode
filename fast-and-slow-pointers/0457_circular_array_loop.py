def circular_array_loop(nums):
    for i in range(len(nums)):
        forward = nums[i] >= 0  
        slow_pointer, fast_pointer = i, i

        while True:
            slow_pointer = find_next_index(nums, slow_pointer, forward)
            fast_pointer = find_next_index(nums, fast_pointer, forward)
            if (fast_pointer != -1):
                fast_pointer = find_next_index(nums, fast_pointer, forward)
            if slow_pointer == -1 or fast_pointer == -1 or slow_pointer == fast_pointer:
                break

        if slow_pointer != -1 and slow_pointer == fast_pointer:
            return True

    return False

def find_next_index(nums, current_index, forward):
    direction = nums[current_index] >= 0

    if direction is not forward:
        return -1

    next_index = (current_index + nums[current_index]) % len(nums)

    if next_index == current_index:
        return -1

    return next_index

def main():
    nums = [1,2,-1,2,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))
    
    nums = [2,2,-1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))
    
    nums = [2,1,-1,-2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))
    
    nums = [2,-1,1,2,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))
    
    nums = [-1,-2,-3,-4,-5,6]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))
    
    nums = [1,-1,5,1,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(circular_array_loop(nums)))

main()
