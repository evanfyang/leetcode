def substring_with_concatenation_of_all_words(string, words):
    num_words = len(words)
    word_length = len(words[0])
    word_frequency = dict()
    substring = ""
    concatenated_substring_indices = list()

    if num_words == 0 or word_length == 0:
        return list()

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    for i in range((len(string) - num_words * word_length) + 1):
        words_seen = dict()
        for j in range(num_words):
            next_word_index = i + j * word_length
            word = string[next_word_index:next_word_index + word_length]

            if word not in word_frequency:
                break

            if word not in words_seen:
                words_seen[word] = 1
            else:
                words_seen[word] += 1

            if words_seen[word] > word_frequency[word]:
                break

            if j + 1 == num_words:
                concatenated_substring_indices.append(i)

    return concatenated_substring_indices

def main():
    string="catfoxcat"
    words=["cat", "fox"]
    print("Input: " + "string = " + string + ", words = " + words)    
    print("Output: " + substring_with_concatenation_of_all_words(string, words))
    
    string="catcatfoxfox"
    words=["cat", "fox"]
    print("Input: " + "string = " + string + ", words = " + words)    
    print("Output: " + substring_with_concatenation_of_all_words(string, words))
    
    string = "barfoothefoobarman"
    words = ["foo","bar"]
    print("Input: " + "string = " + string + ", words = " + words)    
    print("Output: " + substring_with_concatenation_of_all_words(string, words))
    
    string = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print("Input: " + "string = " + string + ", words = " + words)    
    print("Output: " + substring_with_concatenation_of_all_words(string, words))
    
    string = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print("Input: " + "string = " + string + ", words = " + words)    
    print("Output: " + substring_with_concatenation_of_all_words(string, words))
    
main()
