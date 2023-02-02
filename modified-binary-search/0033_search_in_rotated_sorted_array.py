def search_in_rotated_sorted_array(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (start + end) // 2

        if target == nums[middle]:
            return middle
        
        # this if block handles cases where there are duplicates in nums;
        # the only difference from the solution for all unique numbers is
        # if numbers at indexes start, middle, and end are same, we can't choose a side;
        # the best we can do is to skip one number from both ends as target != nums[middle]
        if nums[start] == nums[middle] and nums[end] == nums[middle]:
            start += 1
            end -= 1
        # left side is sorted in ascending order
        elif nums[start] <= nums[middle]:
            if nums[start] <= target and target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        # right side is sorted in ascending order
        else:
            if nums[middle] < target and target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1
    
    return -1

def main():
    nums = [10,15,1,3,8]
    target = 10
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

    nums = [4,5,7,9,10,-1,2]
    target = 10
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

    nums = [4,5,6,7,0,1,2]
    target = 0
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

    nums = [4,5,6,7,0,1,2]
    target = 3
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

    nums = [1]
    target = 0
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

    nums = [5,1,3]
    target = 3
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(search_in_rotated_sorted_array(nums, target)))
    print()

main()