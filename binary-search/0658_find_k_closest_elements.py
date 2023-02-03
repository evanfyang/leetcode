'''
We compare the distance between target - nums[middle] and nums[middle + k] - target
Assume nums[middle] ~ nums[middle + k] is sliding window

case 1: target - nums[middle] < nums[middle + k] - target, need to move window go left
-------target----nums[middle]-----------------nums[middle + k]----------

case 2: target - nums[middle] < nums[middle + k] - target, need to move window go left again
-------nums[middle]----target-----------------nums[middle + k]----------

case 3: target - nums[middle] > nums[middle + k] - target, need to move window go right
-------nums[middle]------------------target---nums[middle + k]----------

case 4: target - nums[middle] > nums[middle + k] - target, need to move window go right
-------nums[middle]---------------------nums[middle + k]----target------

If target - nums[middle] > nums[middle + k] - target,
it means nums[middle + 1] ~ nums[middle + k] is better than nums[middle] ~ nums[middle + k - 1],
and we have middle smaller than the right i.
So assign left = middle + 1.
'''

def find_k_closest_elements(nums, target, k):
    start, end = 0, len(nums) - k

    while start < end:
        middle = (start + end) // 2
        # if target > (nums[middle + k] + nums[middle]) / 2:
        if target - nums[middle] > nums[middle + k] - target:
            start = middle + 1
        else:
            end = middle
    
    return nums[start:start + k]

def main():
    nums = [1,2,3,4,5]
    target = 3
    k = 4
    print("Input: nums = " + str(nums) + ", target = " + str(target) + ", k = " + str(k))
    print("Output: " + str(find_k_closest_elements(nums, target, k)))
    print()

    nums = [1,2,3,4,5]
    target = -1
    k = 4
    print("Input: nums = " + str(nums) + ", target = " + str(target) + ", k = " + str(k))
    print("Output: " + str(find_k_closest_elements(nums, target, k)))
    print()

main()