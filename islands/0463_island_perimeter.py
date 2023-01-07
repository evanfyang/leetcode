def island_perimeter(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    visited = set()

    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == 1:
                return calculate_perimeter_dfs(matrix, x, y, visited)

def calculate_perimeter_dfs(self, matrix, x, y, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 1
    if matrix[x][y] == 0:
        return 1
    if (x, y) in visited:
        return 0

    visited.add((x, y))

    perimeter = 0 
    perimeter += self.calculate_perimeter_dfs(matrix, x - 1, y, visited)
    perimeter += self.calculate_perimeter_dfs(matrix, x + 1, y, visited)
    perimeter += self.calculate_perimeter_dfs(matrix, x, y - 1, visited)
    perimeter += self.calculate_perimeter_dfs(matrix, x, y + 1, visited)

    return perimeter

def main():
    matrix = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(island_perimeter(matrix)))

    matrix = [[1]]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(island_perimeter(matrix)))
    
    matrix = [[1,0]]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(island_perimeter(matrix)))

main()
