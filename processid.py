from SwSpotify import spotify

def getSong():
    song = spotify.song()
    artist = spotify.artist()
    bio = "I am currently listening to: \n" + song + " \n" + artist + "\nhttps://github.com/tpby2005/spotify-to-twitter"
    return bio