def max_sum_subarray_of_size_k(k, array):
    windowStart, windowSum, maxSum = 0, 0, 0
    
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(windowSum, maxSum)
            windowSum -= array[windowStart]
            windowStart += 1
    
    return maxSum

def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sum_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sum_subarray_of_size_k(2, [2, 3, 4, 1, 5])))

main()
