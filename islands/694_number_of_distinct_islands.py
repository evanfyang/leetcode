def number_of_distinct_islands(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    num_distinct_islands = 0
    visited = set() 
    traversal_sequences = set()
    
    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == 1:
                traversal_sequence = traverse_islands_dfs(matrix, x, y, "O"):
                if traversal_sequence not in traversal_sequences:
                    traversal_sequences.add(traversal_sequence)
                    num_distinct_islands += 1
                    
    return num_distinct_islands

def traverse_islands_dfs(matrix, x, y, visited, direction):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return ""
    if matrix[x][y] == 0 or (x, y) in visited:
        return ""
    
    visited.add((x, y))
    
    traversal_sequence = direction
    traversal_sequence += traverse_islands_dfs(matrix, x - 1, y, visited, "L")
    traversal_sequence += traverse_islands_dfs(matrix, x + 1, y, visited, "R")
    traversal_sequence += traverse_islands_dfs(matrix, x, y - 1, visited, "D")
    traversal_sequence += traverse_islands_dfs(matrix, x, y + 1, visited, "U")
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
