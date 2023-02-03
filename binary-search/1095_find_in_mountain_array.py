def find_in_mountain_array_leetcode(array, target):
    n = array.length()
    
    # find index of peak
    start, end = 0, n - 1
    while start < end:
        middle = (start + end) // 2
        if array.get(middle) < array.get(middle + 1):
            start = peak = middle + 1
        else:
            end = middle
    
    # find target in the left of peak
    start, end = 0, peak
    while start <= end:
        middle = (start + end) // 2
        if array.get(middle) < target:
            start = middle + 1
        elif array.get(middle) > target:
            end = middle - 1
        else:
            return middle
    
    # find target in the right of peak
    start, end = peak, n - 1
    while start <= end:
        middle = (start + end) // 2
        if array.get(middle) > target:
            start = middle + 1
        elif array.get(middle) < target:
            end = middle - 1
        else:
            return middle
    
    return -1


def find_in_mountain_array(array, target):
    max_index = find_max_index(array)
    target_index = binary_search(array, target, 0, max_index)
    
    if target_index != -1:
        return target_index
    
    return binary_search(array, target, max_index + 1, len(array) - 1)


# find index of the maximum value in a bitonic array
def find_max_index(array):
    start, end = 0, len(array) - 1
    
    while start < end:
        middle = start + (end - start) // 2
        if array[middle] > array[middle + 1]:
            end = middle
        else:
            start = middle + 1

    # at the end of the while loop, 'start == end'
    return start


# order-agnostic binary search
def binary_search(array, target, start, end):
    while start <= end:
        middle = int(start + (end - start) / 2)

        if target == array[middle]:
            return middle

        if array[start] < array[end]:  # ascending order
            if target < array[middle]:
                end = middle - 1
            else:  # target > array[middle]
                start = middle + 1
        else:  # descending order
            if target > array[middle]:
                end = middle - 1
            else:  # target < array[middle]
                start = middle + 1

    return -1  # element is not found


def main():
    array = [1,3,8,4,3]
    target = 4
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

    array = [3,8,3,1]
    target = 8
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

    array = [1,3,8,12]
    target = 12
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

    array = [10,9,8]
    target = 10
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

    array = [1,2,3,4,5,3,1]
    target = 13
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

    array = [0,1,2,4,2,1]
    target = 3
    print("Input: array = " + str(array) + ", target = " + str(target))
    print("Output: " + str(find_in_mountain_array(array, target)))
    print()

main()