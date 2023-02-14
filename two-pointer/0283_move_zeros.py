def move_zeroes(nums):
    left, right = 0, 0
    
    for _ in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        
        right += 1

def main():
    nums = [0,1,0,3,12]
    print("Input: nums = " + str(nums))
    move_zeroes(nums)
    print("Output: " + str(nums))
    print()

    nums = [0]
    print("Input: nums = " + str(nums))
    move_zeroes(nums)
    print("Output: " + str(nums))
    print()

main()