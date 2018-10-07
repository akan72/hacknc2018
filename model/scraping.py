
# coding: utf-8

# In[1]:


import pandas as pd
import lyricsgenius as genius
from nltk.corpus import stopwords

api = genius.Genius('Wjaaj3obfMqU5E2v7aIdSS-PyH7CcGCK_-i_tDf6qDxNqGRzc4u5maoWcpi6Pqba')


# In[39]:

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
    
    return lyrics_set


# In[11]:


#code from danielle
def findLyrics():
    rock = ["Imagine Dragons", "lovelytheband", "Panic! At The Disco", "Mumford & Sons", "Bad Wolves", "John Mayer", "twenty one pilots", "George Ezra", "Badflower"]
    latin = ["Nio García", "Luis Fonsi", "6ix9ine", "Nicky Jam", "Daddy Yankee", "Becky G", "Ozuna", "Shakira", "Bad Bunny", "Maluma"]
    hiphop = ["Juice WRLD", "Post Malone", "Drake", "Eminem", "Travis Scott", "Cardi B", "Kanye West", "Tyga", "Drake", "DJ Khaled"]
    country = ["Bebe Rexha","Florida Georgia Line","Dan & Shay","Luke Combs","Kane Brown","Old Dominion", "Russell Dickerson","Luke Bryan","Cole Swindell","Mitchell Tenpenny"]
    christian = ["Lauren Daigle", "Avril Lavigne","Cory Asbury","Hillsong Worship","for KING & COUNTRY", "Tauren Wells","Elevation Worship","TobyMac","Francesca Battiselli","MercyMe"]
    punk = ["Minor Threat","Black Flag","Descendents", "Fugazi","Bad Brains","Dead Kennedys","Rancid","Bad Religion", "Pennywise", "NOFX"]
    
    genres = [('rock',rock), ('latin',latin), ('hiphop',hiphop), ('country',country), ('christian',christian), ('punk',punk)]
    
    master = []
    
    for genre in genres:
        for artist in genre[1]:
            artist = api.search_artist(artist, max_songs=5)
            songList = artist.songs
            for song in songList:
                row = (song.lyrics, genre[0])
                master.append(row)
    return master


def test():
    rock = ["Bad Wolves", "lovelytheband"]
    genres = [('rock',rock)]
    master= []


    for genre in genres:
        for artist in genre[1]:
            artist = api.search_artist(artist, max_songs=5)
            songList = artist.songs
            for song in songList:
                row = (song.lyrics, genre[0])
                master.append(row)
    print("right before return master")
    return master

masterList = findLyrics()
print(masterList)


# In[12]:


output = pd.DataFrame(masterList)
output.to_csv('lyrics.csv')

