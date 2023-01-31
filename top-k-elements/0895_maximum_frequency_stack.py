from heapq import *

class FrequencyStackElement:
    def __init__(self, number, frequency, sequence_number):
        self.number = number
        self.frequency = frequency
        self.sequence_number = sequence_number
    
    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # if both elements have same frequency, return the element that was pushed later
        return self.sequence_number > other.sequence_number

class FrequencyStack:
    def __init__(self):
        self.sequence_number = 0
        self.number_frequency = dict()
        self.max_heap = list()
        
    def push(self, val: int) -> None:
        self.number_frequency[val] = self.number_frequency.get(val, 0) + 1
        heappush(self.max_heap, FrequencyStackElement(val, self.number_frequency[val], self.sequence_number))
        self.sequence_number += 1

    def pop(self) -> int:
        val = heappop(self.max_heap).number
        if self.number_frequency[val] > 1:
            self.number_frequency[val] -= 1
        else:
            del self.number_frequency[val]
        
        return val

def main():
    frequency_stack = FrequencyStack()
    print("Push 1")
    frequency_stack.push(1)
    print("Push 2")
    frequency_stack.push(2)
    print("Push 3")
    frequency_stack.push(3)
    print("Push 2")
    frequency_stack.push(2)
    print("Push 1")
    frequency_stack.push(1)
    print("Push 2")
    frequency_stack.push(2)
    print("Push 5")
    frequency_stack.push(5)
    print("Pop: " + str(frequency_stack.pop()))
    print("Pop: " + str(frequency_stack.pop()))
    print("Pop: " + str(frequency_stack.pop()))
    print()

    frequency_stack = FrequencyStack()
    print("Push 5")
    frequency_stack.push(5)
    print("Push 7")
    frequency_stack.push(7)
    print("Push 5")
    frequency_stack.push(5)
    print("Push 7")
    frequency_stack.push(7)
    print("Push 4")
    frequency_stack.push(4)
    print("Push 5")
    frequency_stack.push(5)
    print("Pop: " + str(frequency_stack.pop()))
    print("Pop: " + str(frequency_stack.pop()))
    print("Pop: " + str(frequency_stack.pop()))
    print("Pop: " + str(frequency_stack.pop()))
    print()

main()