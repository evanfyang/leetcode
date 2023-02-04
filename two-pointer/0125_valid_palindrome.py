def valid_palindrome(string):
    left, right = 0, len(string) - 1
    string = string.lower()

    while left < right:
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1
        
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

def main():
    string = "A man, a plan, a canal: Panama"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_palindrome(string))) 
    print() 

    string = "race a car"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_palindrome(string))) 
    print() 

    string = " "
    print("Input: string = " + str(string))
    print("Output: " + str(valid_palindrome(string))) 
    print() 

    string = "Was it a car or a cat I saw?"
    print("Input: string = " + str(string))
    print("Output: " + str(valid_palindrome(string))) 
    print() 

main()