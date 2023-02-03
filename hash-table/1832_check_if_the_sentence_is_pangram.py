import string

def check_if_the_sentence_is_pangram(sentence):
    character_frequency = dict()
    for character in string.ascii_lowercase:
        character_frequency[character] = 0

    for character in sentence.lower():
        character_frequency[character] = + 1

    for character in character_frequency:
        if character_frequency[character] == 0:
            return False
    
    return True

def main():
    sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = "This is not a pangram"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = "abcdefghijklmnopqrstuvwxyz"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = ""
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

    sentence = "leetcode"
    print("Input: sentence = " + str(sentence))
    print("Output: " + str(check_if_the_sentence_is_pangram(sentence)))
    print()

main()