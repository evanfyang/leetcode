def cycle_in_matrix(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    visited = [[False for j in range(num_columns)] for i in range(num_rows)]

    for x in range(num_rows):
        for y in range(num_columns):
            if not visited[x][y]:
                if contains_cycle_dfs(matrix, visited, matrix[x][y], x, y, -1, -1):
                    return True
    return False

def contains_cycle_dfs(self, matrix, visited, start_character, x, y, previous_x, previous_y): 
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False
    if matrix[x][y] != start_character:
        return False
    if visited[x][y]:
        return True

    visited[x][y] = True

    if previous_x != x - 1 and contains_cycle_dfs(matrix, visited, start_character, x - 1, y, x, y):
        return True
    if previous_x != x + 1 and contains_cycle_dfs(matrix, visited, start_character, x + 1, y, x, y):
        return True
    if previous_y != y - 1 and contains_cycle_dfs(matrix, visited, start_character, x, y - 1, x, y):
        return True
    if previous_y != y + 1 and contains_cycle_dfs(matrix, visited, start_character, x, y + 1, x, y):
        return True

    return False

def main():
    matrix = [
        ["a","a","a","a"],
        ["a","b","b","a"],
        ["a","b","b","a"],
        ["a","a","a","a"]
    ]
    print("Input: " + "matrix = " + str(matrix))
    print("Output: " + str(cycle_in_matrix(matrix)))

    matrix = [
        ["c","c","c","a"],
        ["c","d","c","c"],
        ["c","c","e","c"],
        ["f","c","c","c"]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(cycle_in_matrix(matrix)))
    
    matrix = [
        ["a","b","b"],
        ["b","z","b"],
        ["b","b","a"]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(cycle_in_matrix(matrix)))
    
main()
