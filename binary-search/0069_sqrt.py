def sqrt(number):
    if number < 2:
        return number
    
    left, right = 0, number // 2

    while left <= right:
        middle = (left + right) // 2
        square = middle * middle
        
        if square > number:
            right = middle - 1
        elif square < number:
            left = middle + 1
        else:
            return middle
    
    return right

def main():
    number = 64
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number))) 
    print() 

    number = 32
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number)))  
    print() 

    number = 16
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number)))  
    print() 

    number = 8
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number)))  
    print() 

    number = 4
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number))) 
    print() 

    number = 2
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number))) 
    print() 

    number = 1
    print("Input: number = " + str(number))
    print("Output: " + str(sqrt(number))) 
    print() 

main()