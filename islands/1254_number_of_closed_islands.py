def number_of_closed_islands(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    visited = [[False for j in range(num_columns)] for i in range(num_rows)]
    closed_island_count = 0

    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == 0 and not visited[x][y]:
                if is_closed_island_dfs(matrix, x, y, visited):
                    closed_island_count += 1

    return closed_island_count

def is_closed_island_dfs(matrix, x, y, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False
    if matrix[x][y] == 1 or visited[x][y]:
        return True

    visited[x][y] = True

    island_is_closed = True
    island_is_closed &= is_closed_island_dfs(matrix, x - 1, y, visited)
    island_is_closed &= is_closed_island_dfs(matrix, x + 1, y, visited)
    island_is_closed &= is_closed_island_dfs(matrix, x, y - 1, visited)
    island_is_closed &= is_closed_island_dfs(matrix, x, y + 1, visited)

    return island_is_closed

def main():
    matrix = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(number_of_closed_islands(matrix)))
    
    matrix = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(number_of_closed_islands(matrix)))
  
main()
