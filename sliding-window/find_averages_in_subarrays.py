def find_averages_of_subarrays(k, array):
	result = list()
	windowSum, windowStart = 0, 0
	
	for windowEnd in range(len(array)):
		windowSum += array[windowEnd]
		if windowEnd >= k - 1:
			result.append(windowSum / k)
			windowSum -= array[windowStart]
			windowStart += 1
	
	return result

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()
