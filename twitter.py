import tweepy
import os
from dotenv import load_dotenv
import time
from spotify import getwindow
from processid import getSong
from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

#   authorization

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
#auth.set_access_token(access_token,access_token_secret)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')
print(redirect_url)
verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print('Error! Failed to get access token.')

key = auth.access_token
secret = auth.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
bio = "value"
bio1 = "value1"
closed = True

while True:
    time.sleep(5)
    try:
        bio = getSong()
        while bio != bio1:
            print(bio)
            api.update_profile(
                description = bio
            )
            bio1 = bio
        else:
            continue
    except SpotifyClosed as error:
        print('spotify closed')
        if closed == False:
            api.update_profile(
                description = "Spotify Closed"
            )
            closed = True
        elif closed == True:
            continue
    except SpotifyPaused as error:
        print('spotify paused')
        if closed == False:
            api.update_profile(
                description = "Spotify Paused"
            )
            closed = True
        elif closed == True:
            continue
    except SpotifyNotRunning as error:
        print('spotify not running')
        if closed == False:
            api.update_profile(
                description = "Spotify Not Running"
            )
            closed = True
        elif closed == True:
            continue