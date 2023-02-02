def subset_sum(nums, target_sum):
    nums_length = len(nums)
    dp = [[False for x in range(target_sum + 1)] for y in range(nums_length)]

    # populate the target_sum = 0 columns, as we can always form '0' target_sum with an empty set
    for i in range(0, nums_length):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required target_sum is
    # equal to its value
    for nums_sum in range(1, target_sum + 1):
        dp[0][nums_sum] = True if nums[0] == nums_sum else False

    # process all subsets for all sums
    for i in range(1, nums_length):
        for nums_sum in range(1, target_sum+1):
            # if we can get the target_sum 'nums_sum' without the number at index 'i'
            if dp[i - 1][nums_sum]:
                dp[i][nums_sum] = dp[i - 1][nums_sum]
            elif nums_sum >= nums[i]:
                # else include the number to see if we can find a subset to get the remaining target_sum
                dp[i][nums_sum] = dp[i - 1][nums_sum - nums[i]]

    # the bottom-right corner will have our answer.
    return dp[nums_length - 1][target_sum]

def main():
    nums = [1,2,3,7]
    target_sum = 6
    print("Input: nums = " + str(nums) + ", target_sum = " + str(target_sum))
    print("Output: " + str(subset_sum(nums, target_sum)))
    print()

    nums = [1,2,7,1,5]
    target_sum = 10
    print("Input: nums = " + str(nums) + ", target_sum = " + str(target_sum))
    print("Output: " + str(subset_sum(nums, target_sum)))
    print()

    nums = [1,3,4,8]
    target_sum = 6
    print("Input: nums = " + str(nums) + ", target_sum = " + str(target_sum))
    print("Output: " + str(subset_sum(nums, target_sum)))
    print()

main()