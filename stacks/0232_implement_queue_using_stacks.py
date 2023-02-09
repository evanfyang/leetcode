class Queue:
    def __init__(self):
        self.stack_1 = list()
        self.stack_2 = list()
        self.front = None

    def push(self, element):
        if len(self.stack_1) == 0:
            self.front = element
        
        self.stack_1.append(element)

    def pop(self):
        if len(self.stack_2) == 0:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        
        return self.stack_2.pop()

    def peek(self):
        if self.stack_2:
            return self.stack_2[-1]
        else:
            return self.front

    def empty(self):
        return len(self.stack_1) == 0 and len(self.stack_2) == 0

def main():
    print("implement queue using stacks")
    queue = Queue()
    print("Push 1")
    queue.push(1)
    print("Push 2")
    queue.push(2)
    print("Peek: " + str(queue.peek()))
    print("Pop: " + str(queue.pop())) 
    print("Empty: " + str(queue.empty())) 
    
main()