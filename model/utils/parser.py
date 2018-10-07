def parseLyrics(song_list): 
    song_lyrics_sets = []
    
    for song in song_list:
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
        song_lyrics_sets.append(word_set)
    
        #format stop words as a list so we can remove stop words
        stwords = stopwords.raw()
        stopword_list = stwords.split()

        #Remove stop words
        words_to_remove = []
        for lyrics_set in song_lyrics_sets:
            for lyric in lyrics_set:
                if lyric in stopword_list:
                    words_to_remove.append(lyric)

        words_to_remove = set(words_to_remove)
        for lyrics_set in song_lyrics_sets:
            for word in words_to_remove:
                if word in lyrics_set:
                    lyrics_set.remove(word)

    return song_lyrics_sets