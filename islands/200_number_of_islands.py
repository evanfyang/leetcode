def number_of_islands(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    total_islands = 0

    if not matrix:
        return 0

    for x in range(num_rows):
        for y in range(num_columns):
            if matrix[x][y] == "1":
                total_islands += 1
                visit_islands_dfs(matrix, x, y)

    return total_islands

def visit_islands_dfs(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return
    if matrix[x][y] == '0':
        return

    matrix[x][y] = "0"

    visit_islands_dfs(matrix, x + 1, y)
    visit_islands_dfs(matrix, x - 1, y)
    visit_islands_dfs(matrix, x, y + 1)
    visit_islands_dfs(matrix, x, y - 1)

def main():
    matrix = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(number_of_islands(matrix)))
    
    matrix = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Input: " + "matrix = " + str(matrix))    
    print("Output: " + str(number_of_islands(matrix)))
    
main()
