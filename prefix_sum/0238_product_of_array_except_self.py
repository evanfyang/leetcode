def product_of_array_except_self_linear_space_complexity(nums):
    prefix = [0 for _ in range(len(nums))]
    postfix = [0 for _ in range(len(nums))]
    result = [0 for _ in range(len(nums))]

    for i in range(len(nums)):
        if i == 0:
            prefix[i] = nums[i]
        else:
            prefix[i] = prefix[i - 1] * nums[i]

    for j in range(len(nums) - 1, -1, -1):
        if j == len(nums) - 1:
            postfix[j] = nums[j]
        else:
            postfix[j] = nums[j] * postfix[j + 1]
    
    for k in range(len(nums)):
        if k == 0:
            result[k] = postfix[k + 1]
        elif k == len(nums) - 1:
            result[k] = prefix[k - 1]
        else:
            result[k] = prefix[k - 1] * postfix[k + 1]
    
    return result

def product_of_array_except_self(nums):
    result = [0 for _ in range(len(nums))]

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        result[j] *= postfix
        postfix *= nums[j]

    return result

def main():
    nums = [1,2,3,4]
    print("Input: nums = " + str(nums))
    print("Output: " + str(product_of_array_except_self(nums))) 
    print() 

    nums = [-1,1,0,-3,3]
    print("Input: nums = " + str(nums))
    print("Output: " + str(product_of_array_except_self(nums))) 
    print() 

main()