def three_sum(nums):
    nums.sort()
    triplets = list()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        find_triplets(nums, -nums[i], i + 1, triplets)

    return triplets

def find_triplets(nums, target_sum, left_pointer, triplets):
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:
        current_sum = nums[left_pointer] + nums[right_pointer]
        if current_sum == target_sum:
            triplets.append([-target_sum, nums[left_pointer], nums[right_pointer]])
            left_pointer += 1
            right_pointer -= 1
            while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                left_pointer += 1
            while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                right_pointer -= 1
        elif current_sum > target_sum:
            right_pointer -= 1
        else:
            left_pointer += 1

def main():
    nums = [-1,0,1,2,-1,-4]
    print("Input: nums = " + str(nums))
    print("Output: " + three_sum(nums))
    
    nums = [0,1,1]
    print("Input: nums = " + str(nums))
    print("Output: " + three_sum(nums))
    
    nums = [0,0,0]
    print("Input: nums = " + str(nums))
    print("Output: " + three_sum(nums))

main()
