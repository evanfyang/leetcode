def missing_number_grokking(nums):
    for index in range(len(nums)):
        while nums[index] < len(nums) and nums[index] != index:
            temp = nums[nums[index]]
            nums[nums[index]] = nums[index]
            nums[index] = temp

    for index in range(len(nums)):
        if nums[index] != index:
            return index

    return len(nums)

def missing_number(nums):
    n = len(nums)
    n_sum = (n * (n + 1)) // 2
    nums_sum = 0

    for num in nums:
        nums_sum += num

    return n_sum - nums_sum

def main():
    nums = [4,0,3,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))
    
    nums = [8,3,5,2,4,6,0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))
    
    nums = [3,0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))

    nums = [0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))
    
    nums = [9,6,4,2,3,5,7,0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))
    
main()
