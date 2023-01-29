from heapq import *

def reorganize_string(string):
    character_frequency = dict()
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1
    
    max_heap = list()
    for character, frequency in character_frequency.items():
        heappush(max_heap, (-frequency, character))
    
    result_string = str()
    previous_frequency, previous_character = 0, None
    while max_heap:
        frequency, character = heappop(max_heap)
        if -previous_frequency > 0 and previous_character:
            heappush(max_heap, (previous_frequency, previous_character))
        
        result_string += character
        previous_frequency = frequency + 1
        previous_character = character
    
    return result_string if len(result_string) == len(string) else ""

def main():
    string = "aappp"
    print("Input: string = " + str(string))
    print("Output: " + str(reorganize_string(string)))
    print()

    string = "Programming"
    print("Input: string = " + str(string))
    print("Output: " + str(reorganize_string(string)))
    print()

    string = "aapa"
    print("Input: string = " + str(string))
    print("Output: " + str(reorganize_string(string)))
    print()

    string = "aab"
    print("Input: string = " + str(string))
    print("Output: " + str(reorganize_string(string)))
    print()

    string = "aaab"
    print("Input: string = " + str(string))
    print("Output: " + str(reorganize_string(string)))
    print()

main()