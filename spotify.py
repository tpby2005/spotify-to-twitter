import win32gui
import win32process

def getwindow():
    w = win32gui
    bio = w.GetWindowText (w.GetForegroundWindow())
    return bio