def palindrome_number_linear_space(number):
    number = str(number)

    left_pointer = 0
    right_pointer = len(number) - 1

    while left_pointer < right_pointer:
        if number[left_pointer] != number[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    
    return True

def palindrome_number(number):
    # edge cases: when number < 0,  number is not a palindrome;
    # if the last digit of the number is 0, in order for it to be 
    # a palindrome the first digit of the number also needs to be 0;
    # 0 is the only number that satisfies this property
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    # to avoid overflow of the reversed number (i.e. reversed_number > maximum integer), 
    # only revert half of the  number since the reverse of the last half of the palindrome 
    # should be the same as the first half of the number if the number is a palindrome
    reversed_number = 0
    while number > reversed_number:
        reversed_number = (reversed_number * 10) + (number % 10)
        number //= 10
    
    # when the number of digits in the original number is an odd number, remove the middle digit with reversed_number // 10
    # example: when number is 12321, at the end of the while loop we get number = 12, reversed_number = 123;
    # remove the middle digit since it does not matter in a palidrome (it will always equal to itself)
    return number == reversed_number or number == reversed_number // 10

def main():
    number = 121
    print("Input: number = " + str(number))
    print("Output: " + str(palindrome_number(number))) 
    print()
    
    number = -121
    print("Input: number = " + str(number))
    print("Output: " + str(palindrome_number(number))) 
    print()

    number = 10
    print("Input: number = " + str(number))
    print("Output: " + str(palindrome_number(number))) 
    print()

main()