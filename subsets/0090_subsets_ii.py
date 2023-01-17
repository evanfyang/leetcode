def subsets_ii(nums):
    nums.sort()

    subsets = list()
    subsets.append([])

    start_index, end_index = 0, 0

    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            new_subset = list(subsets[j])
            new_subset.append(nums[i])
            subsets.append(new_subset)
    
    return subsets

def main():
    nums = [1,2,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets_ii(nums)))
    print()

    nums = [0]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets_ii(nums)))
    print()

    nums = [1,3,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets_ii(nums)))
    print()

    nums = [1,5,3,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets_ii(nums)))
    print()

main()