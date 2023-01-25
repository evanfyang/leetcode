def count_rotations(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2

        # if mid is greater than the next element
        if mid < end and nums[mid] > nums[mid + 1]:
            return mid + 1

        # if mid is smaller than the previous element
        if mid > start and nums[mid - 1] > nums[mid]:
            return mid
        # left side is sorted, so the pivot is on right side
        if nums[start] < nums[mid]:  
            start = mid + 1
        # right side is sorted, so the pivot is on the left side
        else:  
            end = mid - 1

    # the array has not been rotated
    return 0

def main():
    nums = [10,15,1,3,8]
    print("Input: nums = " + str(nums))
    print("Output: " + str(count_rotations(nums)))
    print()

    nums = [4,5,7,9,10,-1,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(count_rotations(nums)))
    print()

    nums = [1,3,8,10]
    print("Input: nums = " + str(nums))
    print("Output: " + str(count_rotations(nums)))
    print()

main()  