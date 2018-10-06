import lyricsgenius as genius
api = genius.Genius('Wjaaj3obfMqU5E2v7aIdSS-PyH7CcGCK_-i_tDf6qDxNqGRzc4u5maoWcpi6Pqba')

def findLyrics():

  rock = ["Imagine Dragons", "lovelytheband", "Panic! At The Disco", "Mumford & Sons", "Bad Wolves", "John Mayer", "twenty one pilots", "George Ezra", "Badflower"]
  latin = ["Nio García", "Luis Fonsi", "6ix9ine", "Nicky Jam", "Daddy Yankee", "Becky G", "Ozuna", "Shakira", "Bad Bunny", "Maluma"]
  hiphop = ["Juice WRLD", "Post Malone", "Drake", "Eminem", "Travis Scott", "Cardi B", "Kanye West", "Tyga", "Drake", "DJ Khaled"]
  country = ["Bebe Rexha","Florida Georgia Line","Dan & Shay","Luke Combs","Kane Brown","Old Dominion""Russell Dickerson","Luke Bryan","Cole Swindell","Mitchell Tenpenny"]
  christian = ["Lauren Daigle", "Avril Lavigne","Cory Asbury","Hillsong Worship","for KING & COUNTRY", "Tauren Wells","Elevation Worship","tobyMac","Francesca Battiselli","MercyMe","Rend Collective"]
  punk = ["Minor Threat","Black Flag","Descendents", "Fugazi","Bad Brains","Dead Kennedys","Rancid","Bad Religion", "Pennywise", "NOFX"]

  genres = [rock, latin, hiphop, country, christian, punk]

  master = []

  for genre in genres:
    for artist in genre:
      artist = api.search_artist(artist, max_songs=5)
      songList = artist.songs
      for song in songList:
        songLyrics = api.search_song(song, artist.name)
        row = (songLyrics, genre)
        master.append(row)


def test():

  rock = ["Bad Wolves", "lovelytheband"]
  genres = [rock]

  master= []

  for genre in genres:
    for artist in genre:
      artist = api.search_artist(artist, max_songs=5)
      songList = artist.songs
      for song in songList:
        songLyrics = api.search_song(song, artist.name)
        row = (songLyrics, genre)
        master.append(row)

masterList = test()
print(masterList)
