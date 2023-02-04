def longest_repeating_character_replacement(string, k):
    windowStart, maxRepeatingCharacterCount, maxLength = 0, 0, 0
    characterFrequency = dict()
    
    for windowEnd in range(len(string)):
        if string[windowEnd] not in characterFrequency:
            characterFrequency[string[windowEnd]] = 1
        else:
            characterFrequency[string[windowEnd]] += 1
            
        maxRepeatingCharacterCount = max(maxRepeatingCharacterCount, characterFrequency[string[windowEnd]])
        
        if ((windowEnd - windowStart + 1) - maxRepeatingCharacterCount > k):
            characterFrequency[string[windowStart]] -= 1
            windowStart += 1
            
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    
    return maxLength

def main():
    k = 2
    string = "ABAB"
    print("Input: " + "k = " + k + ", string = " + string)    
    print("Output: " + longest_repeating_character_replacement(string, k))
    
    k = 1
    string = "AABABBA"
    print("Input: " + "k = " + k + ", string = " + string)    
    print("Output: " + longest_repeating_character_replacement(string, k))

main()
