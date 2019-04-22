from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os


class mainWindow:                                                                                   #main window for program

    def __init__(self, master, settings):
        self.settings = settings
        self.master = master
        self.master.title("Airfoil Modification Tool")
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
        settingsTop = Frame(settings)
        settingsTop.pack()
        settingsBottom = Frame(settings)
        settingsBottom.pack()

        closeSettings = Button(settingsBottom, text = "Close", command = settings.destroy)
        closeSettings.grid(row = 0)
        #closeAndSaveSettings = Button(settingsBottom, text = "Close and Save")
        #closeAndSaveSettings.grid(row = 0, column = 1)

        ansysFileLoc = Entry(settingsTop, width = 60)
        ansysLabel = Label(settingsTop, text = "ANSYS Application Location")
        ansysLabel.grid(row = 0)
        ansysFileLoc.grid(row = 0, column = 1)

        ansysFileLoc.insert(0, self.settings.getAnsysLoc())

    def fileLoad(self):
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = self.settings.getCurrentOpenLoc()
        self.fileLocation = filedialog.askopenfilename(initialdir = dir_path,title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        if os.path.dirname(self.fileLocation) != "":
            self.settings.setCurrentOpenLoc(os.path.dirname(self.fileLocation))

    def printFileLocation(self, event):
        print(self.fileLocation)
