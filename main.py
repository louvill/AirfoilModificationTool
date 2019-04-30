from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os

os.system("cls")                                                                                    #clear console

from settingsFile import *                                                                          #settings file
settings = settingsFile()

root = Tk()
from windows import *                                                                               #window class
window = mainWindow(root, settings)
root.mainloop()