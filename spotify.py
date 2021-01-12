import win32gui

def getwindow():
    w = win32gui
    bio = w.GetWindowText (w.GetForegroundWindow())
    return bio