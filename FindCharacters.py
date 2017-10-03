def find_characters(words, char):
    new_list = []
    for i in range(0, len(words)):
        if words[i].find(char) != -1:
            new_list.append(words[i])
    print new_list

word_list = ['hello','world','my','name','is','Anna']

find_characters(word_list, "o")