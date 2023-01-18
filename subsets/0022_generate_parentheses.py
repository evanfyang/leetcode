from collections import deque

class ParenthesesString:
    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count

def generate_parentheses(n):
    parentheses_permutations = list()
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    
    while queue:
        parentheses_string = queue.popleft()
        if parentheses_string.open_count == n and parentheses_string.close_count == n:
            parentheses_permutations.append(parentheses_string.string)
        else:
            if parentheses_string.open_count < n:
                queue.append(ParenthesesString(parentheses_string.string + "(", parentheses_string.open_count + 1, parentheses_string.close_count))
            if parentheses_string.open_count > parentheses_string.close_count:
                queue.append(ParenthesesString(parentheses_string.string + ")", parentheses_string.open_count, parentheses_string.close_count + 1))
    
    return parentheses_permutations

def main():
    n = 0
    print("Input: n = " + str(n))
    print("Output: " + str(generate_parentheses(n)))
    print()

    n = 1
    print("Input: n = " + str(n))
    print("Output: " + str(generate_parentheses(n)))
    print()

    n = 2
    print("Input: n = " + str(n))
    print("Output: " + str(generate_parentheses(n)))
    print()

    n = 3
    print("Input: n = " + str(n))
    print("Output: " + str(generate_parentheses(n)))
    print()

main()