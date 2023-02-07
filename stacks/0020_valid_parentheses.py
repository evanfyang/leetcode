def valid_parentheses(string):
    brackets = {")":"(", "}":"{", "]":"["}
    stack = list()

    for character in string:
        if character in brackets:
            if len(stack) == 0 or stack[-1] != brackets[character]:
                return False
            else:
                stack.pop()
        else:
            stack.append(character)

    return len(stack) == 0

def main():
    string = "()"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_parentheses(string))) 
    print()

    string = "()[]{}"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_parentheses(string))) 
    print()

    string = "(]"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_parentheses(string))) 
    print()

    string = "({[]})"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_parentheses(string))) 
    print()

main()