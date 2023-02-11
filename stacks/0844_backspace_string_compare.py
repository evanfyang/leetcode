def backspace_string_compare_two_pointer(string_1, string_2):
    string_1_index = len(string_1) - 1
    string_2_index = len(string_2) - 1

    while string_1_index >= 0 or string_2_index >= 0:
        next_string_1_index = get_next_valid_character_index(string_1, string_1_index)
        next_string_2_index = get_next_valid_character_index(string_2, string_2_index)

        if next_string_1_index < 0 and next_string_2_index < 0:
            return True
        if next_string_1_index < 0 or next_string_2_index < 0:
            return False
        if string_1[next_string_1_index] != string_2[next_string_2_index]:
            return False

        string_1_index = next_string_1_index - 1
        string_2_index = next_string_2_index - 1

    return True

def get_next_valid_character_index(string, index):
    backspace_count = 0

    while index >= 0:
        if string[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1

    return index

def build_string(string):
    result_string = list()
    for character in string:
        if character != "#":
            result_string.append(character)
        else:
            result_string.pop()

    return "".join(result_string)

def backspace_string_compare(string_1, string_2):
    return build_string(string_1) == build_string(string_2)

def main():
    string_1 = "xy#z"
    string_2 = "xzz#"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))
    
    string_1 = "xy#z"
    string_2 = "xyz#"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))
    
    string_1 = "xp#"
    string_2 = "xyz##"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))

    string_1 = "xywrrmp"
    string_2 = "xywrrmu#p"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))

    string_1 = "ab#c"
    string_2 = "ad#c"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))
    
    string_1 = "ab##"
    string_2 = "c#d#"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))
    
    string_1 = "a#c"
    string_2 = "b"
    print("Input: string_1 = " + string_1 + ", string_2 = " + string_2)
    print("Output: " + str(backspace_string_compare(string_1, string_2)))
    
main()
