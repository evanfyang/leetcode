def max_area_of_islands(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    max_island_area = 0

    if not matrix:
        return 0

    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == 1:
                island_area = visit_islands_dfs(matrix, x, y)
                max_island_area = max(max_island_area, island_area)

    return max_island_area

def visit_island_dfs(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 0
    if matrix[x][y] == 0:
        return 0

    island_area = 1
    matrix[x][y] = 0

    island_area += visit_islands_dfs(matrix, x + 1, y)
    island_area += visit_islands_dfs(matrix, x - 1, y)
    island_area += visit_islands_dfs(matrix, x, y + 1)
    island_area += visit_islands_dfs(matrix, x, y - 1)

    return island_area

def main():
    matrix = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(max_area_of_islands(matrix)))
    
    matrix = [
        [0,0,0,0,0,0,0,0]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(max_area_of_islands(matrix)))
    
main()
