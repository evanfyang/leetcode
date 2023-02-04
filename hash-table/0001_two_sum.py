def two_sum(nums, target):
    hash_table = dict()

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        else:
            hash_table[nums[i]] = i

    return list()

def main():
    nums = [2,7,11,15]
    target = 9
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(two_sum(nums, target))) 
    print()

    nums = [3,2,4]
    target = 6
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(two_sum(nums, target))) 
    print()

    nums = [3,3]
    target = 6
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(two_sum(nums, target))) 
    print()

main()