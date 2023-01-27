def single_number_iii(nums):
    # get the XOR of the all the numbers; since there are two of every number 
    # in nums except for the two numbers we are looking for, all the double 
    # numbers in nums will cancel each other out to 0 in the XOR operation; 
    # the XOR of all numbers in nums is just the XOR of the two numbers we
    # are looking for
    num1_xor_num2 = 0        
    for num in nums:
        num1_xor_num2 ^= num
    
    # get the rightmost bit that is a '1' in the XOR of the two numbers we are
    # looking for, num1 and num2; since num1 and num2 are two different numbers,
    # they will differ in their binary representation in at least one position;
    # we will use the rightmost_set_bit to seperate the two numbers
    rightmost_set_bit = 1
    while rightmost_set_bit & num1_xor_num2 == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    
    # seperate all the numbers in nums into two groups; in each group, there are 
    # two of each number except for the two numbers we are looking for; applying 
    # the XOR operation to all the numbers in each group will will cancel each 
    # other out to 0 in the XOR operation except for the two numbers we are looking 
    # for in each number
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost_set_bit != 0:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]

def main():
    nums = [1,4,2,1,3,5,6,2,3,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number_iii(nums)))
    print()

    nums = [2,1,3,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number_iii(nums)))
    print()

    nums = [1,2,1,3,2,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number_iii(nums)))
    print()

    nums = [-1,0]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number_iii(nums)))
    print()

    nums = [0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(single_number_iii(nums)))
    print()

main()