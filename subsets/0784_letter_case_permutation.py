from collections import deque

def letter_case_permutation(string):
    permutations_list = list()
    permutations_list.append(string)
    
    for i in range(len(string)):
        if string[i].isalpha():
            permutations_list_length = len(permutations_list)
            for j in range(permutations_list_length):
                new_permutation = list(permutations_list[j])
                new_permutation[i] = new_permutation[i].swapcase()
                permutations_list.append(''.join(new_permutation))

    return permutations_list 

def main():
    string = "ad52"
    print("Input: nums = " + str(string))
    print("Output: " + str(letter_case_permutation(string)))
    print()

    string = "ab7c"
    print("Input: nums = " + str(string))
    print("Output: " + str(letter_case_permutation(string)))
    print()

    string = "a1b2"
    print("Input: nums = " + str(string))
    print("Output: " + str(letter_case_permutation(string)))
    print()

    string = "3z4"
    print("Input: nums = " + str(string))
    print("Output: " + str(letter_case_permutation(string)))
    print()

main()
