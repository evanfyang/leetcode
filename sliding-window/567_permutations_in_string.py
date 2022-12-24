def permutations_in_string(string, pattern):
    windowStart, matched_chars = 0, 0
    char_frequency = dict()

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    for windowEnd in range(len(string)):
        if string[windowEnd] in char_frequency:
            char_frequency[string[windowEnd]] -= 1
            if char_frequency[string[windowEnd]] == 0:
                matched_chars += 1

        if matched_chars == len(char_frequency):
            return True

        if (windowEnd + 1 >= len(pattern)):
            if string[windowStart] in char_frequency:
                if char_frequency[string[windowStart]] == 0:
                    matched_chars -= 1
                char_frequency[string[windowStart]] += 1
            windowStart += 1

    return False

def main():
    string = "eidbaooo"
    pattern = "ab"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + permutations_in_string(string, pattern))
    
    string = "eidboaoo"
    pattern = "ab"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + permutations_in_string(string, pattern))

main()
    
