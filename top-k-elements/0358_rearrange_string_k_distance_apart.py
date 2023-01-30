from heapq import *
from collections import deque

def rearrange_string_k_distance_apart(string, k):
    if k <= 1:
        return string
    
    character_frequency = dict()
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1
    
    max_heap = list()
    for character, frequency in character_frequency.items():
        heappush(max_heap, (-frequency, character))
    
    queue = deque()
    result_string = str()
    while max_heap:
        frequency, character = heappop(max_heap)
        result_string += character
        queue.append((frequency + 1, character))
        if len(queue) == k:
            frequency, character = queue.popleft()
            if -frequency > 0:
                heappush(max_heap, (frequency, character))
    
    return result_string if len(result_string) == len(string) else ""
    
def main():
    string = "mmpp"
    k = 2
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "Programming"
    k = 3
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "aab"
    k = 2
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "aappa"
    k = 3
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "aabbcc"
    k = 3
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "aaabc"
    k = 3
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

    string = "aaadbbcc"
    k = 2
    print("Input: string = " + str(string) + ", k = " + str(k))
    print("Output: " + str(rearrange_string_k_distance_apart(string, k)))
    print()

main()