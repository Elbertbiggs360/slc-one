word = "olly olly in come free"

def word_count(word):
    values = word.split()
    word_dictionary = {}
    for i in values:
        if i in word_dictionary.keys():
            word_dictionary[i] +=1
        else:
            word_dictionary[i] = 1

    return word_dictionary
