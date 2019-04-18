from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os

os.system('cls')                                                                                    #clear console

root = Tk()
from windows import mainWindow
window = mainWindow(root)
root.mainloop()