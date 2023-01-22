def minimum_difference_element(nums, target):
    if target < nums[0]:
        return nums[0]
    
    if target > nums[len(nums) - 1]:
        return nums[len(nums) - 1]
    
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (start + end) // 2

        if target < nums[middle]:
            end = middle - 1
        elif target > nums[middle]:
            start = middle + 1
        else:
            return nums[middle]
    
    # at the end of the while loop, 'start == end + 1'
    #  we are not able to find the element in the given array
    #  return the element which is closest to the 'key'
    if (nums[start] - target) < (target - nums[end]):
        return nums[start]
    else:
        return nums[end]

def main():
    nums = [4,6,10]
    target = 7
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(minimum_difference_element(nums, target)))
    print()

    nums = [4,6,10]
    target = 4
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(minimum_difference_element(nums, target)))
    print()

    nums = [1,3,8,10,15]
    target = 12
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(minimum_difference_element(nums, target)))
    print()

main()