import spacy
import pandas
import lyricsgenius as genius
api = genius.Genius('Wjaaj3obfMqU5E2v7aIdSS-PyH7CcGCK_-i_tDf6qDxNqGRzc4u5maoWcpi6Pqba')
artist = api.search_artist('Andy Shauf', max_songs=3)

song = api.search_song("Chlorine")
print(song)