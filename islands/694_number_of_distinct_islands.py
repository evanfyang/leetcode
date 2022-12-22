def number_of_distinct_islands(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    visited = [[False for j in range(num_columns)] for i in range(num_rows)]
    traversal_sequences = set()

    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == 1 and not visited[x][y]:
                traversal_sequence = traverse_islands_dfs(matrix, x, y, visited, "O")
                traversal_sequences.add(traversal_sequence)
    print(traversal_sequences)
    return len(travel_sequences)

def traverse_islands_dfs(matrix, x, y, visited, direction):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return ""
    if matrix[x][y] == 0 or visited[x][y]:
        return ""

    visited[x][y] = True

    traversal_sequence = direction
    traversal_sequence += traverse_islands_dfs(matrix, x - 1, y, visited, "U")
    traversal_sequence += traverse_islands_dfs(matrix, x + 1, y, visited, "D")
    traversal_sequence += traverse_islands_dfs(matrix, x, y - 1, visited, "L")
    traversal_sequence += traverse_islands_dfs(matrix, x, y + 1, visited, "R")
    traversal_sequence += "B"

    return traversal_sequence

def main():
    matrix = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1]
    ]
    print("Input: " + "matrix = " + str(matrix))
    print("Output: " + str(number_of_distinct_islands(matrix)))

    matrix = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(number_of_distinct_islands(matrix)))
    
main()
