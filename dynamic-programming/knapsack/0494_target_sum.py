def target_sum(nums, target):
    total_sum = sum(nums)

    # if 's + totalSum' is odd, we cannot find a subset with the sum equal 
    # to '(s + totalSum) / 2'
    if total_sum < target or (target + total_sum) % 2 == 1:
        return 0

    return count_of_subset_sum(nums, (target + total_sum) // 2)

def count_of_subset_sum(nums, target):
    nums_length = len(nums)
    dp = [[-1 for x in range(target + 1)] for y in range(nums_length)]

    # populate the target = 0 columns, as we will always have an empty set for zero target
    for i in range(0, nums_length):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required target is
    # equal to its value
    for nums_sum in range(1, target + 1):
        dp[0][nums_sum] = 1 if nums[0] == nums_sum else 0

    # process all subsets for all sums
    for i in range(1, nums_length):
        for nums_sum in range(1, target + 1):
            # exclude the number
            dp[i][nums_sum] = dp[i - 1][nums_sum]
            # include the number, if it does not exceed the target
            if nums_sum >= nums[i]:
                dp[i][nums_sum] += dp[i - 1][nums_sum - nums[i]]

    # the bottom-right corner will have our answer.
    return dp[nums_length - 1][target]

from collections import Counter

def target_sum_leetcode(nums, target):
    count = Counter({0: 1})
    for x in nums:
        step = Counter()
        for y in count:
            step[y + x] += count[y]
            step[y - x] += count[y]
        count = step
    return count[target]

def main():
    nums = [1,1,2,3]
    target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(target_sum(nums, target)))
    print()

    nums = [1,2,7,1]
    target = 9
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(target_sum(nums, target)))
    print()

    nums = [1,1,1,1,1]
    target = 3
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(target_sum(nums, target)))
    print()

    nums = [1]
    target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(target_sum(nums, target)))
    print()

    nums = [0,0,0,0,0,0,0,0,1]
    target = 1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(target_sum_leetcode(nums, target)))
    print()

main()