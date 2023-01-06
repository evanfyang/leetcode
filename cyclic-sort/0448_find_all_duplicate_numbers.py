def find_all_duplicate_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    duplicate_numbers = list()

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers

def main():
    nums = [4,3,2,7,8,2,3,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_duplicate_numbers(nums)))
    
    nums = [1,1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_duplicate_numbers(nums)))
    
    nums = [1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_duplicate_numbers(nums)))
    
    nums = [3,4,4,5,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_duplicate_numbers(nums)))
    
    nums = [5,4,7,2,3,5,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_duplicate_numbers(nums)))

main()
