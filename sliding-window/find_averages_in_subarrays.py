def find_averages_of_subarrays(k, array):
    averages = list()
    windowSum, windowStart = 0, 0
    
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        if windowEnd >= k - 1:
            averages.append(windowSum / k)
            windowSum -= array[windowStart]
            windowStart += 1
    
    return averages

def main():
    k = 5, array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print("Input: " + "k = " + k + ", array = " + array)
    print("Output: " + find_averages_of_subarrays(k, array))

main()
