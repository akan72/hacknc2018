
# coding: utf-8

# In[ ]:

def parseLyrics(song): 
    word_list = song.split()
    list_copy = word_list
    for idx in range(len(word_list)):
        word = word_list[idx]

        #remove punctuation '?' and '.'
        if word.find('?')!= -1:
            word_list[idx] = word.replace("?","")
        if word.find('.') != -1:
            word_list[idx] = word.replace(".","")
        if word.find('\n') != -1:
            word_list[idx] = word.replace("\n","")
        if word.find('\r') != -1:
            word_list[idx] = word.replace("\r","")

    words_to_remove = []
    for word in word_list:
        #remove all part of song headers i.e. [Intro] or [Chorus]
        if word.find('[') != -1:
            words_to_remove.append(word)
        elif word.find(']') != -1:
            words_to_remove.append(word)

    for word in words_to_remove:
        word_list.remove(word)
    word_set = set(word_list)

    return word_set

