
def find_first_and_last_position_of_element_in_sorted_array(nums, target):
    start, end = 0, 1
    search_range = [-1, -1]
    
    search_range[start] = binary_search(nums, target, False)
    
    if search_range[start] != -1:
        search_range[end] = binary_search(nums, target, True)
    
    return search_range

def binary_search(nums, target, find_max_boundary_index):
    start, end = 0, len(nums) - 1
    target_boundary_index = -1

    while start <= end:
        middle = (start + end) // 2

        if target < nums[middle]:
            end = middle - 1
        elif target > nums[middle]:
            start = middle + 1
        else: # target == nums[middle]
            target_boundary_index = middle
            if find_max_boundary_index:
                start = middle + 1
            else:
                end = middle - 1
    
    return target_boundary_index  

def main():
    nums = [4,6,6,6,9]
    target = 6
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

    nums = [1,3,8,10,15]
    target = 10
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

    nums = [1,3,8,10,15]
    target = 12
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

    nums = [5,7,7,8,8,10]
    target = 8
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

    nums = [5,7,7,8,8,10]
    target = 6
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

    nums = []
    target = 0
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(find_first_and_last_position_of_element_in_sorted_array(nums, target)))
    print()

main()