def set_mismatch(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            mismatched_set = [nums[i], i + 1]

    return mismatched_set


def main():
    nums = [1,2,2,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(set_mismatch(nums)))
    
    nums = [1,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(set_mismatch(nums)))
    
    nums = [3,1,2,5,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(set_mismatch(nums)))
    
    nums = [3,1,2,3,6,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(set_mismatch(nums)))

main()
