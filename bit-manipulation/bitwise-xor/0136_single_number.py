def single_number(nums):
    missing_number = 0

    for num in nums:
        missing_number = missing_number ^ num

    return missing_number

def main():
    nums = [1,4,2,1,3,2,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number(nums)))
    print()

    nums = [7,9,7]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number(nums)))
    print()

    nums = [2,2,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number(nums)))
    print()

    nums = [4,1,2,1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number(nums)))
    print()

    nums = [1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number(nums)))
    print()

main()