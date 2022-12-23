 def reverse_string(string):
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer < right_pointer:
        left_character = string[left_pointer]
        s[left_pointer] = string[right_pointer]
        s[right_pointer] = left_character
        left_pointer += 1
        right_pointer -= 1

 def main():
    string = ["h","e","l","l","o"]
    print("Input: string = " + str(string))
    reverse_string(string)
    print("Output: " + str(string))
    
    string = ["H","a","n","n","a","h"]
    print("Input: string = " + str(string))
    reverse_string(string)
    print("Output: " + str(string))

main()
