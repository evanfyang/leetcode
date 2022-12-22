def three_sum_closest(nums, target):
    nums.sort()
    smallest_difference = math.inf

    for i in range(len(nums) - 2):
        left_pointer = i + 1
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            target_difference = target - (nums[i] + nums[left_pointer] + nums[right_pointer])
            if target_difference == 0:
                return target

            if abs(target_difference) < abs(smallest_difference):  
                smallest_difference = target_difference

            if target_difference > 0:
                left_pointer += 1
            else: 
                right_pointer -= 1

    return target - smallest_difference

def main():
    nums = [-1,2,1,-4], target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + three_sum_closest(nums, target))
    
    nums = [0,0,0], target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + three_sum_closest(nums, target))
    
    nums = [-2,0,1,2], target = 2
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + three_sum_closest(nums, target))
    
main()
