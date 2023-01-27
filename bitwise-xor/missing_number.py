def missing_number(nums):
    # add one to length of nums to account for the missing number
    n = len(nums) + 1 
    xor_1_to_n = 1

    for i in range(2, n + 1):
        xor_1_to_n ^= i
    
    xor_nums = nums[0]
    for i in range(1, n - 1):
        xor_nums ^= nums[i]
    
    return xor_1_to_n ^ xor_nums

def main():
    nums = [1,5,2,6,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(missing_number(nums)))
    print()

main()