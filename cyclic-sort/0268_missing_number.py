def missing_number_leetcode(nums):
    n = len(nums)
    n_sum = (n * (n + 1)) // 2
    nums_sum = 0

    for num in nums:
        nums_sum += num

    return n_sum - nums_sum

def missing_number_grokking(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index, that will be our required number
    for i in range(n):
        if nums[i] != i:
            return i

    return n

def missing_number(nums):
    for index in range(len(nums)):
        while nums[index] < len(nums) and nums[index] != index:
            temp = nums[nums[index]]
            nums[nums[index]] = nums[index]
            nums[index] = temp

    for index in range(len(nums)):
        if nums[index] != index:
            return index

    return len(nums)

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
