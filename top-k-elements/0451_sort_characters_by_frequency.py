from heapq import *

def sort_characters_by_frequency(string):
    character_frequency = dict()
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1
    
    max_heap = list()
    for character, frequency in character_frequency.items():
        heappush(max_heap, (-frequency, character))
    
    characters_sorted_by_frequency = str()
    while max_heap:
        frequency, character = heappop(max_heap)
        for _ in range(-frequency):
            characters_sorted_by_frequency += character
    
    return characters_sorted_by_frequency

def main():
    string = "Programming"
    print("Input: string = " + str(string))
    print("Output: " + str(sort_characters_by_frequency(string)))
    print()

    string = "abcbab"
    print("Input: string = " + str(string))
    print("Output: " + str(sort_characters_by_frequency(string)))
    print()

    string = "tree"
    print("Input: string = " + str(string))
    print("Output: " + str(sort_characters_by_frequency(string)))
    print()

    string = "cccaaa"
    print("Input: string = " + str(string))
    print("Output: " + str(sort_characters_by_frequency(string)))
    print()

    string = "Aabb"
    print("Input: string = " + str(string))
    print("Output: " + str(sort_characters_by_frequency(string)))
    print()

main()