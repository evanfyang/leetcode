def majority_element(nums):
    number_frequency = dict()
    nums_length = len(nums)

    for number in nums:
        number_frequency[number] = number_frequency.get(number, 0) + 1
    
    for number, frequency in number_frequency.items():
        if frequency > nums_length / 2:
            return number
    
    return None

def main():
    nums = [3,2,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(majority_element(nums))) 
    print()

    nums = [2,2,1,1,1,2,2]
    print("Input: nums = " + str(nums))
    print("Output: " + str(majority_element(nums))) 
    print()

main()