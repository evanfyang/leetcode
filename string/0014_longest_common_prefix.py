def longest_common_prefix(strings):
    if len(strings) == 0:
        return ""
    
    prefix = strings[0]
    
    for i in range(1, len(strings)):
        while strings[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if len(prefix) == 0: return ""
    
    return prefix

def main():
    strings = ["flower","flow","flight"]
    print("Input: strings = " + str(strings))
    print("Output: " + str(longest_common_prefix(strings)))
    print()

    strings = ["dog","racecar","car"]
    print("Input: strings = " + str(strings))
    print("Output: " + str(longest_common_prefix(strings)))
    print()

    strings = ["leets","leetcode","leet","leeds"]
    print("Input: strings = " + str(strings))
    print("Output: " + str(longest_common_prefix(strings)))
    print()

main()