def squares_of_sorted_array(nums):
    left_pointer, right_pointer = 0, len(nums) - 1
    squares = list()

    while left_pointer <= right_pointer:
        left_square = nums[left_pointer] ** 2
        right_square = nums[right_pointer] ** 2

        if left_square > right_square:
            squares.append(left_square)
            left_pointer += 1
        else:
            squares.append(right_square)
            right_pointer -= 1
    
    squares.reverse()
    return squares

def main():
    nums = [-4,-1,0,3,10]
    print("Input: nums = " + str(nums))
    print("Output: " + squares_of_sorted_array(nums))
    
    nums = [-7,-3,2,3,11]
    print("Input: nums = " + str(nums))
    print("Output: " + squares_of_sorted_array(nums))
    
main()
