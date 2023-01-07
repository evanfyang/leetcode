def four_sum(nums, target):
    nums.sort()
    quadruplets = list()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            find_quadruplets(nums, i, j, target, quadruplets)

    return quadruplets

def find_quadruplets(nums, i, j, target, quadruplets):
    left_pointer = j + 1
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:
        quadruplet_sum = nums[i] + nums[j] + nums[left_pointer] + nums[right_pointer]
        if quadruplet_sum == target:
            quadruplets.append([nums[i], nums[j], nums[left_pointer], nums[right_pointer]])
            left_pointer += 1
            right_pointer -= 1
            while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                left_pointer += 1
            while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                right_pointer -= 1
        if quadruplet_sum < target:
            left_pointer += 1
        if quadruplet_sum > target:
            right_pointer -= 1

def main():
    nums = [1,0,-1,0,-2,2]
    target = 0
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(four_sum(nums, target)))

    nums = [2,2,2,2,2]
    target = 8
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(four_sum(nums, target)))

    nums = [4,1,2,-1,1,-3]
    target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(four_sum(nums, target)))

    nums = [2,0,-1,1,-2,2]
    target = 2
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(four_sum(nums, target)))

main()