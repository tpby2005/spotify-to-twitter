import tweepy
import os
from dotenv import load_dotenv
import time
from spotify import getwindow
from processid import getSong

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


while True:
    bio = getSong()
    print(bio)
    api.update_profile(
        description = bio
    )
    time.sleep(5)