test_word = "olly olly in come free"

def words(word):
    if isinstance(word, str): 
        values = word.split()
        word_dictionary = {}
        for i in values:
            if i.isdigit():
                i = int(i)
            if i in word_dictionary.keys():
                word_dictionary[i] +=1
            else:
                word_dictionary[i] = 1

        return word_dictionary
    else:
        raise TypeError("Invalid Input")

words(test_word)
