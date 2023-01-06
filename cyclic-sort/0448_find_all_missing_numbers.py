def find_missing_numbers_grokking(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missing_numbers = list()

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers

def find_all_missing_numbers(nums):
    for index in range(len(nums)):
        while nums[index] != nums[nums[index] - 1]:
            temp = nums[nums[index] - 1]
            nums[nums[index] - 1] = nums[index]
            nums[index] = temp

    missing_numbers = list()

    for index in range(len(nums)):
        if nums[index] != index + 1:
            missing_numbers.append(index + 1)

    return missing_numbers

def main():
    nums = [2,3,1,8,2,3,5,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_missing_numbers(nums)))
    
    nums = [2,4,1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_missing_numbers(nums)))
    
    nums = [2,3,2,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_missing_numbers(nums)))

    nums = [4,3,2,7,8,2,3,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_missing_numbers(nums)))
    
    nums = [1,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(find_all_missing_numbers(nums)))
    
main()
