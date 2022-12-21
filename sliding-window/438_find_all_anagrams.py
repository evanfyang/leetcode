def find_all_anagrams(string, pattern):
    windowStart, matched = 0, 0
    char_frequency = dict()
    anagrams = list()

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    for windowEnd in range(len(string)):
        right_char = string[windowEnd]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(pattern):
            anagrams.append(windowStart)

        if windowEnd + 1 >= len(pattern):
            left_char = string[windowStart]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            windowStart += 1

    return anagrams

def main():
    string = "cbaebabacd", pattern = "abc"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "abab", pattern = "ab"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "ppqp", pattern = "pq"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    
    string = "abbcabc", pattern = "abc"
    print("Input: " + "string = " + string + ", pattern = " + pattern)    
    print("Output: " + find_all_anagrams(string, pattern))
    

main()
