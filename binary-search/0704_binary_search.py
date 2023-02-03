def binary_search_grokking(nums, target):
    start, end = 0, len(nums) - 1
    is_ascending = nums[start] < nums[end]
    
    while start <= end:
        middle = (start + end) // 2

        if target == nums[middle]:
            return middle

        if is_ascending:  
            if target < nums[middle]:
                end = middle - 1  
            else: 
                start = middle + 1 
        else: 
            if target > nums[middle]:
                end = middle - 1 
            else:  
                start = middle + 1 

    return -1  

def binary_search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (end + start) // 2
        
        if nums[middle] == target:
            return middle

        if target < nums[middle]:
            end = middle - 1
        else:
            start = middle + 1
        
    return -1

def main():
    nums = [4,6,10]
    target = 10
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(binary_search(nums, target)))
    print()

    nums = [1,2,3,4,5,6,7]
    target = 5
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(binary_search(nums, target)))
    print()

    nums = [10,6,4]
    target = 10
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(binary_search(nums, target)))
    print()

    nums = [10,6,4]
    target = 4
    print("Input: nums = " + str(nums) + ", target = " + str(target))
    print("Output: " + str(binary_search(nums, target)))
    print()

main()