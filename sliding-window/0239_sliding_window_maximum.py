from collections import deque

def sliding_window_maximum(nums, k):
    queue = deque()
    left = right = 0
    sliding_window_maximums = list()

    while right < len(nums):
        # pop all smaller values from queue
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        
        queue.append(right)
        
        # if the left value is out of bounds, remove from window
        if left > queue[0]:
            queue.popleft()

        if (right + 1) >= k:
            sliding_window_maximums.append(nums[queue[0]])
            left += 1
        
        right += 1
    
    return sliding_window_maximums

def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(sliding_window_maximum(nums, k))) 
    print() 

    nums = [1]
    k = 1
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Output: " + str(sliding_window_maximum(nums, k))) 
    print() 

main()