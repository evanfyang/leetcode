import math

def longestSubstringKDistinct(string, k):
    maxLength = -math.inf
    windowStart = 0
    charCount = dict()

    for windowEnd in range(len(string)):
        if not string[windowEnd] in charCount:
            charCount[string[windowEnd]] = 1 
        else:
            charCount[string[windowEnd]] += 1  

        while len(charCount) > k:
            charCount[string[windowStart]] -= 1
            if charCount[string[windowStart]] == 0:
                del charCount[string[windowStart]]
            windowStart += 1
        
        maxLength = max(maxLength, windowEnd + 1 - windowStart)

    return maxLength

string = "cbbebi"
k = 3

print(longestSubstringKDistinct(string, k))
