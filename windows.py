from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os
import ntpath
from airfoil import * 

class mainWindow:                                                                                   #main window for program

    def __init__(self, master, settings):
        self.settings = settings                                                                    #settings information
        self.master = master
        self.master.title("Airfoil Modification Tool")
        self.af = airfoil()                                                                         #airfoil that will be used for analysis and display

        topFrame = Frame(master)                                                                    #subdivisions of UI area
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

        self.fileLocLabel = Label(bottomFrame, text = "Current loaded file name will be displayed here", fg = "Black")
        self.fileLocLabel.pack()                                                                    #label that contains file info

        self.canvas = Canvas(middleFrame, width = 800, height = 400)                                #area that info will be drawn
        self.canvas.pack()
        #self.canvas.create_oval(100, 100, 50, 50, fill = "red")

    def quit(self):                                                                                 #close main window dialog
        answer = tkinter.messagebox.askquestion("Quit?", "Are you sure you want to quit?")
        
        if answer == "yes":
            self.master.destroy()

    def openSettings(self):                                                                         #main settings UI
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

        def saveAnsysLoc():
            if ansysFileLoc.get() != self.settings.getAnsysLoc():
                self.settings.setAnsysLoc(ansysFileLoc.get())

        def findAnsysLoc():
            dir_path = os.path.dirname(self.settings.getAnsysLoc())
            ansysLoc = filedialog.askopenfilename(initialdir = dir_path, title = "Locate ANSYS", filetypes = (("exe files",".exe"),("all files","*.*")))
            if ansysLoc != "":
                ansysFileLoc.delete(0, len(ansysFileLoc.get()))
                ansysFileLoc.insert(0, ansysLoc)

        ansysFileLocSave = Button(settingsTop, text = "Save", command = saveAnsysLoc)
        ansysFileLocFind = Button(settingsTop, text = "Locate", command = findAnsysLoc)
        ansysFileLocFind.grid(row = 0, column = 2)
        ansysFileLocSave.grid(row = 0, column = 3)

    def fileLoad(self):
        dir_path = self.settings.getCurrentOpenLoc()
        self.fileLocation = filedialog.askopenfilename(initialdir = dir_path, title = "Select file", filetypes = (("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
        if os.path.dirname(self.fileLocation) != "":
            self.settings.setCurrentOpenLoc(os.path.dirname(self.fileLocation))
            self.fileLocLabel.config(text = ntpath.basename(self.fileLocation))
        self.af.loadFile(self.fileLocation)

    def getFileLocation(self):
        return self.fileLocation