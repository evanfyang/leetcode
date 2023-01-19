from collections import deque

class AbbreviatedWord:
    def __init__(self, string, start, count):
        self.string = string
        self.start = start
        self.count = count

def generalized_abbreviation(word):
    word_length = len(word)
    abbreviated_words = list()
    queue = deque()
    queue.append(AbbreviatedWord([], 0, 0))

    while queue:
        abbreviated_word = queue.popleft()
        if abbreviated_word.start == word_length:
            if abbreviated_word.count != 0:
                abbreviated_word.string.append(str(abbreviated_word.count))
            abbreviated_words.append("".join(abbreviated_word.string))
        else:
            # increment the abbreviation count so when an abbreviated word
            # is processed after being popped from the queue, the count will 
            # be added as the abbreviation in the next if block
            queue.append(AbbreviatedWord(list(abbreviated_word.string), abbreviated_word.start + 1, abbreviated_word.count + 1))
            # add the abbreviation count as the abbreviation
            if abbreviated_word.count != 0:
                abbreviated_word.string.append(str(abbreviated_word.count))
            # append current character to the abbreviated word
            new_word = list(abbreviated_word.string)
            new_word.append(word[abbreviated_word.start])
            # restart the abbreviation count
            queue.append(AbbreviatedWord(new_word, abbreviated_word.start + 1, 0))
    
    return abbreviated_words

def generalized_abbreviation_recursive(word):
    abbreviated_words = list()
    generate_generalized_abbreviations(word, [], 0, 0, abbreviated_words)
    return abbreviated_words

def generate_generalized_abbreviations(word, abbreviated_word, start, count, abbreviated_words):
    if start == len(word):
        if count != 0:
            abbreviated_word.append(str(count))
        abbreviated_words.append(''.join(abbreviated_word))
    else:
        # continue abbreviating by incrementing the current abbreviation count
        generate_generalized_abbreviations(word, list(abbreviated_word), start + 1, count + 1, abbreviated_words)

        # restart abbreviating, append the count and the current character to the string
        if count != 0:
            abbreviated_word.append(str(count))
        new_word = list(abbreviated_word)
        new_word.append(word[start])
        generate_generalized_abbreviations(word, new_word, start + 1, 0, abbreviated_words)

def main():
    word = "BAT"
    print("Input: word = " + str(word))
    print("Output: " + str(generalized_abbreviation_recursive(word)))
    print()

main()