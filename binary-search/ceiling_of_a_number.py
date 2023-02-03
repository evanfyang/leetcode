def ceiling_of_a_number(nums, target):
    start, end = 0, len(nums) - 1

    # if the 'key' is bigger than the biggest element
    if target > nums[end]:
        return -1

    while start <= end:
        middle = (start + end) // 2

        if target < nums[middle]:
            end = middle -1
        elif target > nums[middle]:
            start = middle + 1
        else:
            return middle
    
    # since the loop is running until 'start <= end', so at the end of the while loop, 
    # 'start == end + 1' we are not able to find the element in the given array, so the next
    # big number will be arr[start]
    return start

def main():
    nums = [4,6,10]
    target = 6
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(ceiling_of_a_number(nums, target)))
    print()

    nums = [1,3,8,10,15]
    target = 12
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(ceiling_of_a_number(nums, target)))
    print()

    nums = [4,6,10]
    target = 17
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(ceiling_of_a_number(nums, target)))
    print()

    nums = [4,6,10]
    target = -1
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(ceiling_of_a_number(nums, target)))
    print()

main()
