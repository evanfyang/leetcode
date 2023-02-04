def shortest_word_distance(words, word1, word2):
    shortest_distance = len(words)
    position1, position2 = -1, -1

    for i in range(len(words)):
        if words[i] == word1:
            position1 = i
        if words[i] == word2:
            position2 = i
        if position1 != -1 and position2 != -1:
            shortest_distance = min(shortest_distance, abs(position1 - position2))
    
    return shortest_distance

def main():
    words = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]
    word1 = "fox"
    word2 = "dog"
    print("Input: words = " + str(words) + ", word1 = " + str(word1) + ", word2 = " + str(word2))
    print("Output: " + str(shortest_word_distance(words, word1, word2))) 
    print() 

    words = ["a","c","d","b","a"]
    word1 = "a"
    word2 = "b"
    print("Input: words = " + str(words) + ", word1 = " + str(word1) + ", word2 = " + str(word2))
    print("Output: " + str(shortest_word_distance(words, word1, word2))) 
    print() 

    words = ["a","b","c","d","e"]
    word1 = "a"
    word2 = "e"
    print("Input: words = " + str(words) + ", word1 = " + str(word1) + ", word2 = " + str(word2))
    print("Output: " + str(shortest_word_distance(words, word1, word2))) 
    print() 

    words = ["practice","makes","perfect","coding","makes"]
    word1 = "coding"
    word2 = "practice"
    print("Input: words = " + str(words) + ", word1 = " + str(word1) + ", word2 = " + str(word2))
    print("Output: " + str(shortest_word_distance(words, word1, word2))) 
    print() 

    words = ["practice","makes","perfect","coding","makes"]
    word1 = "makes"
    word2 = "coding"
    print("Input: words = " + str(words) + ", word1 = " + str(word1) + ", word2 = " + str(word2))
    print("Output: " + str(shortest_word_distance(words, word1, word2))) 
    print() 

main()