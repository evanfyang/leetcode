from collections import defaultdict

def group_anagrams(strings):        
    grouped_anagrams = defaultdict(list)

    for string in strings:
        character_count = [0] * 26
        for character in string:
            character_count[ord(character.lower()) - ord("a")] += 1
        grouped_anagrams[tuple(character_count)].append(string)

    return list(grouped_anagrams.values())

def main():
    strings = ["eat","tea","tan","ate","nat","bat"]
    print("Input: strings = " + str(strings))
    print("Output: " + str(group_anagrams(strings))) 
    print()

    strings = [""]
    print("Input: strings = " + str(strings))
    print("Output: " + str(group_anagrams(strings))) 
    print()

    strings = ["a"]
    print("Input: strings = " + str(strings))
    print("Output: " + str(group_anagrams(strings))) 
    print()

main()