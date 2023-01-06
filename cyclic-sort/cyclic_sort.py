def cyclic_sort_grokking(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums

def cyclic_sort(nums):
    for index in range(len(nums)):
        while nums[index] - 1 != index:
            temp = nums[nums[index] - 1]
            nums[nums[index] - 1] = nums[index]
            nums[index] = temp
    return nums

def main():
    nums = [3,1,5,4,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(cyclic_sort(nums)))
    
    nums = [2,6,4,3,1,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(cyclic_sort(nums)))
    
    nums = [1,5,6,4,3,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(cyclic_sort(nums)))

main()
