from collections import deque

def alien_dictionary(words):
    sorted_order = str()
    if len(words) == 0:
        return sorted_order
    
    graph = dict()
    in_degree = dict()
    for word in words:
        for character in word:
            graph[character] = list()
            in_degree[character] = 0

    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            parent, child = word1[j], word2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break
    
    sources = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            sources.append(vertex)
    
    while sources:
        vertex = sources.popleft()
        sorted_order += str(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
            
    if len(sorted_order) != len(in_degree):
        return str()
    
    return sorted_order

def main():
    words = ["ba","bc","ac","cab"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

    words = ["cab","aaa","aab"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

    words = ["ywx","wz","xww","xz","zyy","zwz"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

    words = ["wrt","wrf","er","ett","rftt"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

    words = ["z","x"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

    words = ["we","ee","we"]
    print("Input: words = " + str(words))
    print("Output: " + str(alien_dictionary(words)))
    print()

main()