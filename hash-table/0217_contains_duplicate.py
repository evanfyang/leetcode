def contains_duplicate(nums):
    unique_numbers = set()
    for number in nums:
        if number not in unique_numbers:
            unique_numbers.add(number)
        else:
            return True
    return False

def main():
    nums = [1,2,3,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(contains_duplicate(nums)))

    nums = [1,2,3,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(contains_duplicate(nums)))

    nums = [1,1,1,3,3,4,3,2,4,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(contains_duplicate(nums)))

main()