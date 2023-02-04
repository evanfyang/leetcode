def can_construct_ransom_note(ransom_note, magazine):
    ransom_note_character_frequency = dict()
    magazine_character_frequency = dict()

    for character in ransom_note:
        ransom_note_character_frequency[character] = ransom_note_character_frequency.get(character, 0) + 1
    
    for character in magazine:
        magazine_character_frequency[character] = magazine_character_frequency.get(character, 0) + 1
    
    for character, frequency in ransom_note_character_frequency.items():
        if character not in magazine_character_frequency:
            return False
        if magazine_character_frequency[character] < frequency:
            return False
    
    return True

def main():
    ransom_note = "a"
    magazine = "b"
    print("Input: ransom_note = " + str(ransom_note) + ", magazine = " + str(magazine))
    print("Output: " + str(can_construct_ransom_note(ransom_note, magazine))) 
    print()

    ransom_note = "aa"
    magazine = "ab"
    print("Input: ransom_note = " + str(ransom_note) + ", magazine = " + str(magazine))
    print("Output: " + str(can_construct_ransom_note(ransom_note, magazine))) 
    print()

    ransom_note = "aa"
    magazine = "aab"
    print("Input: ransom_note = " + str(ransom_note) + ", magazine = " + str(magazine))
    print("Output: " + str(can_construct_ransom_note(ransom_note, magazine))) 
    print()

    ransom_note = "bg"
    magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    print("Input: ransom_note = " + str(ransom_note) + ", magazine = " + str(magazine))
    print("Output: " + str(can_construct_ransom_note(ransom_note, magazine))) 
    print()

main()