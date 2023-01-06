def find_duplicate_number(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1

def main():
    nums = [1,3,4,2,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_duplicate_number(nums)))
    
    nums = [3,1,3,4,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_duplicate_number(nums)))
    
    nums = [1,4,4,3,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_duplicate_number(nums)))
    
    nums = [2,1,3,3,5,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_duplicate_number(nums)))
    
    nums = [2,4,1,4,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_duplicate_number(nums)))

main()
