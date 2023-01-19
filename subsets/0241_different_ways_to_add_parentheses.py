def different_ways_to_add_parentheses(expression):
    answers = list()
    if "+" not in expression and "-" not in expression and "*" not in expression:
        answers.append(int(expression))
    else:
        for index in range(len(expression)):
            character = expression[index]
            if not character.isdigit():
                left_part = different_ways_to_add_parentheses(expression[0:index])
                right_part = different_ways_to_add_parentheses(expression[index + 1:])

                for left_number in left_part:
                    for right_number in right_part:
                        if character == "+":
                            answers.append(left_number + right_number)
                        elif character == "-":
                            answers.append(left_number - right_number)
                        elif character == "*":
                            answers.append(left_number * right_number)
    
    return answers

def main():
    expression = "2-1-1"
    print("Input: expression = " + str(expression))
    print("Output: " + str(different_ways_to_add_parentheses(expression)))
    print()

    expression = "2*3-4*5"
    print("Input: expression = " + str(expression))
    print("Output: " + str(different_ways_to_add_parentheses(expression)))
    print()

    expression = "1+2*3"
    print("Input: expression = " + str(expression))
    print("Output: " + str(different_ways_to_add_parentheses(expression)))
    print()

    expression = "2*3-4-5"
    print("Input: expression = " + str(expression))
    print("Output: " + str(different_ways_to_add_parentheses(expression)))
    print()

main()