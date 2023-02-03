def peak_index_in_a_mountain_array(array):
    start, end = 0, len(array) - 1

    while start < end:
        middle = (start + end) // 2
        if array[middle] > array[middle + 1]:
            end = middle
        else:
            start = middle + 1
    
    return start

def main():
    array = [1,3,8,12,4,2]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [3,8,3,1]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [1,3,8,12]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [10,9,8]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [1,0,1]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [0,2,1,0]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

    array = [0,10,5,2]
    print("Input: array = " + str(array))
    print("Output: " + str(peak_index_in_a_mountain_array(array)))
    print()

main()