def longest_palindrome(string):
    character_frequency = dict()
    longest_palindrome_length = 0

    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1
    
    for character, frequency in character_frequency.items():
        # every character that has an even count can be paired 
        # every character that has an odd count can be paired except for one
        longest_palindrome_length += frequency // 2 * 2
        # check if a unique center has been added to longest palindrome count
        # if not (i.e. longest palindrome length is even) and the current character
        # count is odd, use this character as the unique center of the longest
        # palindrome by adding 1 tothe length of longest palindrome
        if longest_palindrome_length % 2 == 0 and frequency % 2 == 1:
            longest_palindrome_length += 1

    return longest_palindrome_length

def main():
    string = "abccccdd"
    print("Input: string = " + str(string))
    print("Output: " + str(longest_palindrome(string))) 
    print()

    string = "a"
    print("Input: string = " + str(string))
    print("Output: " + str(longest_palindrome(string))) 
    print()

    string = "aaabbbccccddddddddeeeeeff"
    print("Input: string = " + str(string))
    print("Output: " + str(longest_palindrome(string))) 
    print()

main()