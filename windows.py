from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os


class mainWindow:                                                                                   #main window for program

    def __init__(self, master, settings):
        self.settings = settings
        self.master = master
        topFrame = Frame(master)
        topFrame.pack(side = TOP)
        middleFrame = Frame(master, height = 200, width = 400)
        middleFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack(side = BOTTOM)

        self.fileLocation = ""                                                                      #init file location to empty

        self.menu = Menu(topFrame)                                                                  #menu across top of window
        master.config(menu=self.menu)

        self.fileSubMenu = Menu(self.menu, tearoff = False)
        self.menu.add_cascade(label = "File", menu = self.fileSubMenu)
        self.fileSubMenu.add_command(label = "Save", command = self.openSettings)
        self.fileSubMenu.add_command(label = "Load...", command = self.fileLoad)
        self.fileSubMenu.add_separator()
        self.fileSubMenu.add_command(label = "Settings", command = self.openSettings)
        self.fileSubMenu.add_separator()
        self.fileSubMenu.add_command(label = "Quit", command = self.quit)

        self.fileLocButton = Button(bottomFrame, text = "Test File Location", fg = "Black")
        self.fileLocButton.pack()
        self.fileLocButton.bind("<Button-1>", self.printFileLocation)

    def test(self):
        print("test")

    def quit(self):
        answer = tkinter.messagebox.askquestion("Quit?", "Are you sure you want to quit?")
        
        if answer == "yes":
            self.master.destroy()

    def openSettings(self):
        settings = Toplevel()
        settings.title("Settings Menu")
        closeSettings = Button(settings, text = "Close", command = settings.destroy)
        closeSettings.pack()

    def fileLoad(self):
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = self.settings.getCurrentOpenLoc()
        self.fileLocation = filedialog.askopenfilename(initialdir = dir_path,title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        self.settings.setCurrentOpenLoc(os.path.dirname(self.fileLocation))

    def printFileLocation(self, event):
        print(self.fileLocation)
