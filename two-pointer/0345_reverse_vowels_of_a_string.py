def reverse_vowels_of_a_string(string):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    left, right = 0, len(string) - 1
    result_string = list(string)

    while left < right:
        while left < right and result_string[left] not in vowels:
            left += 1
        while left < right and result_string[right] not in vowels:
            right -= 1
        
        result_string[left], result_string[right] = result_string[right], result_string[left]
        left += 1
        right -= 1

    return "".join(result_string)

def main():
    string = "hello"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print() 

    string = "AEIOU"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print() 

    string = "DesignGUrus"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print() 

    string = "leetcode"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print() 

    string = "aA"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print()

    string = ".a"
    print("Input: sting = " + str(string))
    print("Output: " + str(reverse_vowels_of_a_string(string))) 
    print()

main()