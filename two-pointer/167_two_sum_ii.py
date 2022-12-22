def two_sum_ii(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        if numbers[left_pointer] + numbers[right_pointer] < target:
            left_pointer += 1
        if numbers[left_pointer] + numbers[right_pointer] > target:
            right_pointer -= 1
        if numbers[left_pointer] + numbers[right_pointer] == target:
            return [left_pointer, right_pointer]
    
    return [-1, -1]

def main():
    numbers = [1, 2, 3, 4, 6], target = 6
    print("Input: " + str(numbers) + ", target: " + str(target))
    print("Output: " + two_sum_ii(numbers, target))
    
    numbers = [2, 5, 9, 11], target = 11
    print("Input: " + str(numbers) + ", target: " + str(target))
    print("Output: " + two_sum_ii(numbers, target))
    
main()
