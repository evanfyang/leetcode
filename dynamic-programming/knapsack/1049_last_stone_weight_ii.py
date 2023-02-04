def minimum_subset_sum_difference(nums):
    nums_sum = sum(nums)
    nums_length = len(nums)
    dp = [[False for x in range(int(nums_sum / 2) + 1)] for y in range(nums_length)]

    # populate the nums_sum=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, nums_length):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to 
    # that number
    for j in range(0, int(nums_sum / 2) + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, nums_length):
        for j in range(1, int(nums_sum / 2) + 1):
            # if we can get the sum 'nums_sum' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                # else include the number and see if we can find a subset to get remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]

    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(nums_sum / 2), -1, -1):
        if dp[nums_length - 1][i]:
            sum1 = i
            break

    sum2 = nums_sum - sum1
    return abs(sum2 - sum1)

def last_stone_weight_ii(stones):
    dp = {0}
    total_stone_weights = sum(stones)
    for stone in stones:
        dp |= {stone + i for i in dp}
    return min(abs(total_stone_weights - i - i) for i in dp)

def main():
    nums = [1,2,3,9]
    print("Input: nums = " + str(nums))
    print("Output: " + str(last_stone_weight_ii(nums)))
    print()

    nums = [1,2,7,1,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(last_stone_weight_ii(nums)))
    print()

    nums = [1,3,100,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(last_stone_weight_ii(nums)))
    print()

    nums = [2,7,4,1,8,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(last_stone_weight_ii(nums)))
    print()

    nums = [31,26,33,21,40]
    print("Input: nums = " + str(nums))
    print("Output: " + str(last_stone_weight_ii(nums)))
    print()

main()