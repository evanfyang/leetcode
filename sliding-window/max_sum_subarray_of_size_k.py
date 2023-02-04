def max_sum_subarray_of_size_k(array, k):
    windowStart, windowSum, maxSum = 0, 0, 0
    
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(windowSum, maxSum)
            windowSum -= array[windowStart]
            windowStart += 1
    
    return maxSum

def main():
    k = 3 
    array = [2, 1, 5, 1, 3, 2]
    print("Input: " + "k = " + k + ", string = " + array)
    print("Output: " + max_sum_subarray_of_size_k(array, k))

    k = 2 
    array = [2, 3, 4, 1, 5]
    print("Input: " + "k = " + k + ", string = " + array)
    print("Output: " + max_sum_subarray_of_size_k(array, k))

main()
