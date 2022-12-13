def longest_substring_with_distinct_characters(string):
    windowStart = 0, maxLength = 0
    characters = dict()

    for windowEnd in range(len(string)):
        if string[windowEnd] not in characters:
            characters[string[windowEnd]] = 1
        else:
            characters[string[windowEnd]] += 1
            while characters[string[windowEnd]] > 1:
                characters[string[windowStart]] -= 1
                if characters[string[windowStart]] == 0:
                    del characters[string[windowStart]]
                windowStart += 1

        maxLength = max(maxLength, windowEnd + 1 - windowStart)

    return maxLength

# example to explain tricky part
# perdawkzvestkou
def longest_substring_with_distinct_characters_grokking_solution(string):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning
        # so that we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # this is tricky; in the current window, we will not have any 'right_char' after
            # its previous index and if 'window_start' is already ahead of the last index of
            # 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

def main():
    string = "abcabcbb"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))
    
    string = "bbbbb"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))
    
    string = "pwwkew"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))
    
    string = "aabccbb"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))
    
    string = "abbbb"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))
    
    string = "abccde"
    print("Input: " + "string = " + string)    
    print("Output: " + longest_substring_with_distinct_characters(string))

main()
