from tkinter import *
from tkinter import messagebox
import tweepy

def window():

    def end():
        api.update_profile(
            description = "Spotify is closed!\n\n\nhttps://github.com/tpby2005/spotify-to-twitter"
            )
        quit()

    tkWindow = Tk()  
    tkWindow.geometry('400x150')  
    tkWindow.title('PythonExamples.org - Tkinter Example')

    button = Button(tkWindow,
        text = 'Submit',
        command = end)  
    button.pack()  
    
    tkWindow.mainloop()
    return window