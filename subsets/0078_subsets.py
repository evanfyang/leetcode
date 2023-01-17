def subsets(nums):
    subsets = list()
    subsets.append([])

    for number in nums:
        subsets_length = len(subsets)
        for index in range(subsets_length):
            new_subset = list(subsets[index])
            new_subset.append(number)
            subsets.append(new_subset)
    
    return subsets

def main():
    nums = [1,2,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets(nums)))
    print()

    nums = [0]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets(nums)))
    print()

    nums = [1,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets(nums)))
    print()

    nums = [1,5,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(subsets(nums)))
    print()

main()