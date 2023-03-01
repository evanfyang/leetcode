class MinStack:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, val if len(self.min_stack) == 0 else self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]

def main():
    min_stack = MinStack()
    print("Push -2")
    min_stack.push(-2)
    print("Push 0")
    min_stack.push(0)
    print("Push -3")
    min_stack.push(-3)
    print("Get Min: " + str(min_stack.get_min()))
    print("Pop")
    min_stack.pop();
    print("Top: " + str(min_stack.top()))
    print("Get Min: " + str(min_stack.get_min()))
    print()
          
main()