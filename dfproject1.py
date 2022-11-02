
import webbrowser
import pyautogui
import os
import time
from tkinter import *

os.system ('timeout /t > nul 0 && cls')

root = Tk ()

root.title ('https://dfproject1.000webhostapp.com/')
root.geometry ('500x250')
root.resizable (False, False)
root.iconbitmap ('icon/icon.ico')
root.minsize (width = 380, height = 180)
root.maxsize (width = 380, height = 180)

def open_website ():
	
    webbrowser.open ('chrome.exe')
    time.sleep (1.5)
    pyautogui.write ('https://dfproject1.000webhostapp.com/')
    time.sleep (0.5)
    pyautogui.press ('enter')

def open_website_by_FTP ():

    webbrowser.open ('chrome.exe')
    time.sleep (1.5)
    pyautogui.write ('https://files.000webhost.com/')
    time.sleep (0.5)
    pyautogui.press ('enter')

def close_browser ():

    os.system ('taskkill /f /im chrome.exe && cls')
    time.sleep (0.5)

open_website = Button (root, text='Open website', command=open_website).pack (pady=15)
open_website = Button (root, text='Open website by FTP', command=open_website_by_FTP).pack (pady=15)
close_website = Button (root, text='Close browser', command=close_browser).pack (pady=15)

root = mainloop ()
