def partition_equal_subset_sum_brute_force(nums):
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    return partition_equal_subset_sum_brute_force_recursive(nums, nums_sum / 2, 0)

def partition_equal_subset_sum_brute_force_recursive(nums, nums_sum, current_index):
    # base check
    if nums_sum == 0:
        return True

    nums_length = len(nums)
    if nums_length == 0 or current_index >= nums_length:
        return False

    # recursive call after choosing the number at the `current_index`
    # if the number at `current_index` exceeds the sum, we shouldn't process this
    if nums[current_index] <= nums_sum:
        if(partition_equal_subset_sum_brute_force_recursive(nums, nums_sum - nums[current_index], current_index + 1)):
            return True

    # recursive call after excluding the number at the 'current_index'
    return partition_equal_subset_sum_brute_force_recursive(nums, nums_sum, current_index + 1)

def partition_equal_subset_sum_memoization(nums):
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    
    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(int(nums_sum / 2) + 1)] for y in range(len(nums))]
    return partition_equal_subset_sum_memoization_recursive(dp, nums, nums_sum, 0)

def partition_equal_subset_sum_memoization_recursive(dp, nums, nums_sum, current_index):
    # base case
    if nums_sum == 0:
        return 1

    nums_length = len(nums)
    if nums_length == 0 or current_index >= nums_length:
        return 0

    # if we have not already processed a similar problem
    if dp[current_index][nums_sum] == -1:
        # recursive call after choosing the number at the current_index
        # if the number at current_index exceeds the nums_sum, we shouldn't process this
        if nums[current_index] <= nums_sum:
            if partition_equal_subset_sum_memoization_recursive(dp, nums, nums_sum - nums[current_index], current_index + 1) == 1:
                dp[current_index][nums_sum] = 1
                return 1

        # recursive call after excluding the number at the current_index
        dp[current_index][nums_sum] = partition_equal_subset_sum_memoization_recursive(dp, nums, nums_sum, current_index + 1)

    return dp[current_index][nums_sum]

def partition_equal_subset_sum_bottom_up_dynamic_programming(nums):
    nums_sum = sum(nums)

    # if 'nums_sum' is a an odd number, we can't have two subsets with same total
    if nums_sum % 2 != 0:
        return False

    # we are trying to find a subset of given numbers that has a total sum of 'nums_sum / 2'.
    nums_sum = int(nums_sum / 2)

    nums_length = len(nums)
    dp = [[False for x in range(nums_sum + 1)] for y in range(nums_length)]

    # populate the nums_sum=0 columns, as we can always for '0' sum with an empty set
    for i in range(0, nums_length):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, nums_sum + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, nums_length):
        for j in range(1, nums_sum + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:  # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]

    # the bottom-right corner will have our answer.
    return dp[nums_length - 1][nums_sum]

def main():
    nums = [1,2,3,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(partition_equal_subset_sum_bottom_up_dynamic_programming(nums)))
    print()

    nums = [1,1,3,4,7]
    print("Input: nums = " + str(nums))
    print("Output: " + str(partition_equal_subset_sum_bottom_up_dynamic_programming(nums)))
    print()

    nums = [2,3,4,6]
    print("Input: nums = " + str(nums))
    print("Output: " + str(partition_equal_subset_sum_bottom_up_dynamic_programming(nums)))
    print()

    nums = [1,5,11,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(partition_equal_subset_sum_bottom_up_dynamic_programming(nums)))
    print()

    nums = [1,2,3,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(partition_equal_subset_sum_bottom_up_dynamic_programming(nums)))
    print()

main()