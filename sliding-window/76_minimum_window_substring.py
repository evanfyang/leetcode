def minimum_window_substring(string, pattern):
    window_start, substring_start, matched = 0, 0, 0
    min_length = len(string) + 1
    character_frequency = dict()

    for character in pattern:
        if character not in character_frequency:
            character_frequency[character] = 1
        else:
            character_frequency[character] += 1

    for window_end in range(len(string)):
        right_character = string[window_end]
        if right_character in character_frequency:
            character_frequency[right_character] -= 1
            if character_frequency[right_character] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substring_start = window_start

            left_character = string[window_start]
            if left_character in character_frequency:
                if character_frequency[left_character] == 0:
                    matched -= 1
                character_frequency[left_character] += 1
            window_start += 1

    if min_length > len(string):
        return ""
    return s[substring_start:substring_start + min_length]

def main():
    def main():
    string = "ADOBECODEBANC", pattern = "ABC"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "a", pattern = "a"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "a", pattern = "aa"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "aabdec", pattern = "abc"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "aabdec", pattern = "abac"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "abdbca", pattern = "abc"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "adcad", pattern = "abc"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
main()
