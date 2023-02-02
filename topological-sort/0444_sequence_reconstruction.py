from collections import deque

def sequence_reconstruction(original_sequence, sequences):
    sorted_order = list()
    if len(original_sequence) <= 0:
        return False
    
    in_degree = dict()
    graph = dict()
    for sequence in sequences:
        for number in sequence:
            in_degree[number] = 0
            graph[number] = list()
    
    for sequence in sequences:
        for i in range(len(sequence) - 1):
            parent, child = sequence[i], sequence[i + 1]
            in_degree[child] += 1
            graph[parent].append(child)
    
    # if we don't have ordering rules for all the numbers we'll not 
    # able to uniquely construct the sequence
    if len(original_sequence) != len(in_degree):
        return False
    
    sources = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            sources.append(vertex)
    
    while sources:
        # more than one source vertex means that there is more than 
        # one way to reconstruct the sequence
        if len(sources) > 1:
            return False
        
        # the next number in sources is different from the number at 
        # the corresponding spot in the original sequence
        if original_sequence[len(sorted_order)] != sources[0]:
            return False
        
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    # if the size of sorted_order is not equal to the size of 
    # original_sequence, there is no unique way to construct the 
    # original_sequence from the sequences given
    return len(original_sequence) == len(sorted_order)

def main():
    original_sequence = [1,2,3,4]
    sequences = [[1,2],[2,3],[3,4]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [1,2,3,4]
    sequences = [[1,2],[2,3],[2,4]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [3,1,4,2,5]
    sequences = [[3,1,5],[1,4,2,5]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [1,2,3]
    sequences = [[1,2],[1,3]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [1,2,3]
    sequences = [[1,2]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [1,2,3]
    sequences = [[1,2],[1,3],[2,3]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

    original_sequence = [4,1,5,2,6,3]
    sequences = [[5,2,6,3],[4,1,5,2]]
    print("Input: original_sequence = " + str(original_sequence) + ", sequences = " + str(sequences))
    print("Output: " + str(sequence_reconstruction(original_sequence, sequences)))
    print()

main()