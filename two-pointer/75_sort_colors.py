def sort_colors(colors):
    RED, WHITE, BLUE = 0, 1, 2

    left_pointer = 0
    right_pointer = len(colors) - 1
    middle_pointer = 0

    while middle_pointer <= right_pointer:
        if colors[middle_pointer] == RED:
            colors[middle_pointer], colors[left_pointer] = colors[left_pointer], colors[middle_pointer]
            middle_pointer += 1
            left_pointer += 1
        elif colors[middle_pointer] == WHITE:
            middle_pointer += 1
        elif colors[middle_pointer] == BLUE:
            colors[middle_pointer], colors[right_pointer] = colors[right_pointer], colors[middle_pointer]
            right_pointer -= 1

def main():
    colors = [1,0,2,1,0]
    print("Input: colors = " + str(colors))
    sort_colors(colors)
    print("Output: " + str(colors))

    colors = [2,2,0,1,2,0]
    print("Input: colors = " + str(colors))
    sort_colors(colors)
    print("Output: " + str(colors))

    colors = [2,0,2,1,1,0]
    print("Input: colors = " + str(colors))
    sort_colors(colors)
    print("Output: " + str(colors))

    colors = [2,0,1]
    print("Input: colors = " + str(colors))
    sort_colors(colors)
    print("Output: " + str(colors))

main()
