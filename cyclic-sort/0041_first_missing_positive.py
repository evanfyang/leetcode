def first_missing_positive(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] >= 0 and nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

def main():
    nums = [-3,1,5,4,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()
    
    nums = [3,-2,0,1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()
    
    nums = [3,2,5,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()

    nums = [33,37,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()    

    nums = [1,2,0]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()

    nums = [1,2,0]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()    

    nums = [3,4,-1,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()

    nums = [7,8,9,11,12]
    print("Input: nums = " + str(nums))
    print("Output: " + str(first_missing_positive(nums)))
    print()

main()
