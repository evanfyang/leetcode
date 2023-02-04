def number_of_good_pairs(nums):
    number_frequency = dict()
    pair_count = 0

    for number in nums:
        if number not in number_frequency:
            number_frequency[number] = 1
        else:
            pair_count += number_frequency[number]
            number_frequency[number] += 1

    return pair_count

def main():
    nums = [1,2,3,1,1,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(number_of_good_pairs(nums))) 
    print() 

    nums = [1,1,1,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(number_of_good_pairs(nums))) 
    print() 

    nums = [1,2,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(number_of_good_pairs(nums))) 
    print() 

main()