def three_sum_smaller(nums, target):
    nums.sort()
    count = 0

    for i in range(len(nums)):
        count = count_sums_smaller(nums, target - nums[i], i)
    
    return count

def count_sums_smaller(nums, target_sum, first_number_idx):
    count = 0
    left_pointer = first_number_idx + 1
    right_pointer = len(nums)

    while left_pointer < right_pointer:
        if nums[left_pointer] + nums[right_pointer] < target_sum:
            count += right_pointer - left_pointer
            left_pointer += 1
        else:
            right_pointer -= 1

    return count

def main():
    nums = [-1,0,2,3]
    target = 3
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + three_sum_smaller(nums, target))
    
    nums = [-1,4,2,1,3]
    target = 5
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + three_sum_smaller(nums, target))

main()