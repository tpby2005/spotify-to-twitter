from SwSpotify import spotify

def getSong():
    song = spotify.song()
    artist = spotify.artist()
    bio = "I am currently listening to: \n" + song + " \n" + artist
    return bio