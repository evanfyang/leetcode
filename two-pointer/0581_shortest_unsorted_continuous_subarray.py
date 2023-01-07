def find_unsorted_subarray(nums):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < len(nums) - 1 and nums[left_pointer] <= nums[left_pointer + 1]:
        left_pointer += 1

    if left_pointer == len(nums) - 1:
        return 0

    while right_pointer > 0 and nums[right_pointer] >= nums[right_pointer - 1]:
        right_pointer -= 1

    subarray_minimum = math.inf
    subarray_maximum = -math.inf

    for i in range(left_pointer, right_pointer + 1):
        subarray_minimum = min(subarray_minimum, nums[i])
        subarray_maximum = max(subarray_maximum, nums[i])

    while left_pointer > 0 and nums[left_pointer - 1] > subarray_minimum:
        left_pointer -= 1

    while right_pointer < len(nums) - 1 and nums[right_pointer + 1] < subarray_maximum:
        right_pointer += 1

    return right_pointer - left_pointer + 1

def main():
    nums = [1,2,5,3,7,10,9,12]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))

    nums = [1,3,2,0,-1,7,10]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))
    
    nums = [1,2,3]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))

    nums = [3,2,1]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))

    nums = [2,6,4,8,10,9,15]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))
    
    nums = [1,2,3,4]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))
    
    nums = [1]
    print("Input: nums = " + nums)
    print("Output: " + str(find_unsorted_subarray(nums)))    

main()
