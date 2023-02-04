def count_of_subset_sum(nums, target_sum):
    nums_length = len(nums)
    dp = [[-1 for x in range(target_sum + 1)] for y in range(nums_length)]

    # populate the target_sum = 0 columns, as we will always have an empty set for zero target_sum
    for i in range(0, nums_length):
        dp[i][0] = 1

    # with only one number, we can form a subset only when the required target_sum is
    # equal to its value
    for nums_sum in range(1, target_sum + 1):
        dp[0][nums_sum] = 1 if nums[0] == nums_sum else 0

    # process all subsets for all sums
    for i in range(1, nums_length):
        for nums_sum in range(1, target_sum + 1):
            # exclude the number
            dp[i][nums_sum] = dp[i - 1][nums_sum]
            # include the number, if it does not exceed the target_sum
            if nums_sum >= nums[i]:
                dp[i][nums_sum] += dp[i - 1][nums_sum - nums[i]]

    # the bottom-right corner will have our answer.
    return dp[nums_length - 1][target_sum]

def main():
    nums = [1,1,2,3]
    target_sum = 4
    print("Input: nums = " + str(nums) + ", target_sum = " + str(target_sum))
    print("Output: " + str(count_of_subset_sum(nums, target_sum)))
    print()

    nums = [1,2,7,1,5]
    target_sum = 9
    print("Input: nums = " + str(nums) + ", target_sum = " + str(target_sum))
    print("Output: " + str(count_of_subset_sum(nums, target_sum)))
    print()

main() 