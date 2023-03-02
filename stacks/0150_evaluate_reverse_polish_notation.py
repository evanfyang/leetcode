import operator

def evaluate_reverse_polish_notation(tokens):
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    stack = list()

    for token in tokens:
        if token in operators:
            right_operand = stack.pop()
            left_operand = stack.pop()
            result = operators[token](left_operand, right_operand)
            stack.append(int(result))
        else:
            stack.append(int(token))
    
    return stack[-1]

def main():
    tokens = ["2","1","+","3","*"]
    print("Input: tokens = " + str(tokens))
    print("Output: " + str(evaluate_reverse_polish_notation(tokens)))
    print()

    tokens = ["4","13","5","/","+"]
    print("Input: tokens = " + str(tokens))
    print("Output: " + str(evaluate_reverse_polish_notation(tokens)))
    print()

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print("Input: tokens = " + str(tokens))
    print("Output: " + str(evaluate_reverse_polish_notation(tokens)))
    print()

main()