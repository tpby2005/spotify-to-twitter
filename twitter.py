import tweepy
import os
from dotenv import load_dotenv
import time
from spotify import getwindow
from processid import getSong
from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused
from tkinter import *
from tkinter import messagebox
import keyboard

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
argument = 4
argument1 = 4


def run():
    bio = "value"
    bio1 = "value1"
    argument = 4
    argument1 = 4
    while True:
        argument1 = argument
        time.sleep(5)
        try:
            bio = getSong()
            while bio != bio1:
                print(bio)
                api.update_profile(
                    description=bio
                )
                bio1 = bio
            else:
                continue
        except SpotifyClosed as error:
            argument = 1
        except SpotifyPaused as error:
            argument = 2

    while argument == 1:
        while argument != argument1:
            api.update_profile(
                description = "Spotify Closed!"
                )
            argument1 = 1
    while argument == 2:
        while argument != argument1:
            api.update_profile(
                description = "Spotify Paused!"
                )
            argument1 = 2


def valueswitcher():
    switcher = {
        0: "Playing",
        1: "Closed",
        2: "Paused",
        3: "Not Playing"
    }
    return switcher.get(argument, "nothing")

def end():
    api.update_profile(
        description = "Spotify is closed!\n\n\nhttps://github.com/tpby2005/spotify-to-twitter"
        )
    quit()

while True:
    if keyboard.is_pressed(']'):
        gui()
    else:
        run()

def gui():
    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('Spotify To Twitter')

    button = Button(tkWindow,
        text = 'Quit',
        command = end)  
    button2 = Button(tkWindow,
        text = 'Run',
        command = run)  
    button.pack()
    button2.pack()

    tkWindow.mainloop()
    tkWindow.destroy()

# while True:
#     time.sleep(5)
#     try:
#         bio = getSong()
#         while bio != bio1:
#             print(bio)
#             api.update_profile(
#                 description = bio
#             )
#             bio1 = bio
#         else:
#             continue
#     except SpotifyClosed as error:
#         print('spotify closed')
#         if closed == False:
#             api.update_profile(
#                 description = "Spotify Closed"
#             )
#             closed = True
#         elif closed == True:
#             continue
#     except SpotifyPaused as error:
#         print('spotify paused')
#         if closed == False:
#             api.update_profile(
#                 description = "Spotify Paused"
#             )
#             closed = True
#         elif closed == True:
#             continue
#     except SpotifyNotRunning as error:
#         print('spotify not running')
#         if closed == False:
#             api.update_profile(
#                 description = "Spotify Not Running"
#             )
#             closed = True
#         elif closed == True:
#             continue