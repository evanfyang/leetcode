from collections import deque

def permutations_recursive(nums):
    permutations = list()
    generate_permutations(nums, 0, [], permutations)
    return permutations

def generate_permutations(nums, nums_index, current_permutation, permutations):
    # current_permutation is complete since it is 
    # the same length as nums, append to list of
    # permutations to return
    if nums_index == len(nums):
        permutations.append(current_permutation)
    else:
        # add number at num_index of nums to every position of current_permutation;
        # call the generate_permutations function on the new current_permutation 
        # to add the number at num_index + 1 of nums to every position of the
        # new current_permutation
        for index in range(len(current_permutation) + 1):
            new_permutation = list(current_permutation)
            new_permutation.insert(index, nums[nums_index])
            generate_permutations(nums, nums_index + 1, new_permutation, permutations)

def permutations(nums):
    permutations = list()
    permutations_queue = deque()
    permutations_queue.append([])

    for number in nums:
        # this keeps the range of the next for loop constant 
        permutations_queue_length = len(permutations_queue)

        # remove each incomplete permutation in the permutation
        # queue to add a new number to each position   
        for _ in range(permutations_queue_length):
            old_permutation = permutations_queue.popleft()
            
            # create a new permutation from adding the new 
            # number to each position in the old incomplete 
            # permutation 
            for index in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(index, number)
                
                # if the new permutation matches the length of 
                # original numbers, add to list of permutations 
                # to return; otherwise, add it back to the 
                # incomplete permutation queue
                if len(new_permutation) == len(nums):
                    permutations.append(new_permutation)
                else:
                    permutations_queue.append(new_permutation)
    
    return permutations

def main():
    nums = [1,3,5]
    print("Input: nums = " + str(nums))
    print("Output: " + str(permutations(nums)))
    print()

    nums = [1,2,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(permutations(nums)))
    print()

    nums = [0,1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(permutations(nums)))
    print()

    nums = [1]
    print("Input: nums = " + str(nums))
    print("Output: " + str(permutations(nums)))
    print()

main()