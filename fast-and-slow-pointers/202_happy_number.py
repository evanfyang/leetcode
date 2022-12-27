def happy_number(number):
    slow_pointer = number
    fast_pointer = self.find_squared_sum(number)

    while slow_pointer != fast_pointer:
        slow_pointer = self.find_squared_sum(slow_pointer)
        fast_pointer = self.find_squared_sum(self.find_squared_sum(fast_pointer))
        if slow_pointer == fast_pointer:
            break

    return slow_pointer == 1

def find_squared_sum(self, number):
    squared_sum = 0
    while number > 0:
        digit = number % 10
        squared_sum += digit ** 2
        number //= 10
    return squared_sum

def main():
    number = 23
    print("Input: " + str(number))
    print("Output: " + str(happy_number(number)))
    
    number = 12
    print("Input: " + str(number))
    print("Output: " + str(happy_number(number)))
    
    number = 19
    print("Input: " + str(number))
    print("Output: " + str(happy_number(number)))

    number = 2
    print("Input: " + str(number))
    print("Output: " + str(happy_number(number)))

    number = 1
    print("Input: " + str(number))
    print("Output: " + str(happy_number(number)))
    
main()
