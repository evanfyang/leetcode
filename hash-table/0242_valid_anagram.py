def valid_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    character_frequency = dict()
    for character in string1:
        character_frequency[character] = character_frequency.get(character, 0) + 1
    
    for character in string2:
        character_frequency[character] = character_frequency.get(character, 0) - 1
    
    for character in character_frequency:
        if character_frequency[character] != 0:
            return False
    
    return True

def main():
    string1 = "listen"
    string2 = "silent"
    print("Input: string1 = " + str(string1) + ", string2 = " + str(string2))
    print("Output: " + str(valid_anagram(string1, string2))) 
    print() 

    string1 = "rat"
    string2 = "silent"
    print("Input: string1 = " + str(string1) + ", string2 = " + str(string2))
    print("Output: " + str(valid_anagram(string1, string2))) 
    print() 

    string1 = "hello"
    string2 = "world"
    print("Input: string1 = " + str(string1) + ", string2 = " + str(string2))
    print("Output: " + str(valid_anagram(string1, string2))) 
    print() 

    string1 = "anagram"
    string2 = "nagaram"
    print("Input: string1 = " + str(string1) + ", string2 = " + str(string2))
    print("Output: " + str(valid_anagram(string1, string2))) 
    print() 

    string1 = "rat"
    string2 = "car"
    print("Input: string1 = " + str(string1) + ", string2 = " + str(string2))
    print("Output: " + str(valid_anagram(string1, string2))) 
    print() 

main()
