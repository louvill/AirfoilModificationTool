from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os
import ntpath
from airfoil import * 
import time

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

        self.canvasWidth = 800
        self.canvasHeight = 400
        self.canvas = Canvas(middleFrame, width = self.canvasWidth, height = self.canvasHeight)     #area that info will be drawn
        self.canvas.grid()

        self.randomizeButton = Button(middleFrame, text = "Randomize Geometry", command = self.randomizeAirfoil)
        self.randomizeButton.grid(row = 0, column = 1, padx = 10)
        self.iterationsPerClick = 100
        self.numberOfIterations = 0
        self.iterationsLabel = Label(middleFrame, text = "Number of Iterations: 0")
        self.iterationsLabel.grid(row = 1, column = 1)

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

        ansysFileLoc = Entry(settingsTop, width = len(self.settings.getAnsysLoc())+10)              #ansys file location modification
        ansysLabel = Label(settingsTop, text = "ANSYS Application Location")
        ansysLabel.grid(row = 0)
        ansysFileLoc.grid(row = 0, column = 1)

        ansysFileLoc.insert(0, self.settings.getAnsysLoc())

        def saveAnsysLoc():
            if ansysFileLoc.get() != self.settings.getAnsysLoc() and os.path.exists(ansysFileLoc.get()) == True:
                self.settings.setAnsysLoc(ansysFileLoc.get())                                       #only save if not already present or the same

        def findAnsysLoc():                                                                         #file open dialog
            dir_path = os.path.dirname(self.settings.getAnsysLoc())
            ansysLoc = filedialog.askopenfilename(initialdir = dir_path, title = "Locate ANSYS", filetypes = (("exe files",".exe"),("all files","*.*")))
            if ansysLoc != "":
                ansysFileLoc.delete(0, len(ansysFileLoc.get()))
                ansysFileLoc.insert(0, ansysLoc)
            settings.lift()

        ansysFileLocSave = Button(settingsTop, text = "Save", command = saveAnsysLoc)
        ansysFileLocFind = Button(settingsTop, text = "Locate", command = findAnsysLoc)
        ansysFileLocFind.grid(row = 0, column = 2)
        ansysFileLocSave.grid(row = 0, column = 3)

    def fileLoad(self):                                                                             #runs to load csv into airfoil object and display window
        dir_path = self.settings.getCurrentOpenLoc()
        self.fileLocation = filedialog.askopenfilename(initialdir = dir_path, title = "Select file", filetypes = (("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
        if os.path.dirname(self.fileLocation) != "":
            self.settings.setCurrentOpenLoc(os.path.dirname(self.fileLocation))
            self.fileLocLabel.config(text = ntpath.basename(self.fileLocation))
            self.af.loadFile(self.fileLocation)
            self.canvas.delete(ALL)
            self.plotAirfoil()
            self.numberOfIterations = 0
            self.iterationsLabel.config(text = "Number of Iterations: 0")

    def plotAirfoil(self):                                                                          #displays geometry calculated by airfoil object
        points = self.af.getPlottingPoints(self.canvasWidth,self.canvasHeight)
        polypoints = []
        for i in range(0,len(points)):
            polypoints.append(points[i][0])
            polypoints.append(points[i][1])
        self.canvas.create_polygon(polypoints, outline = "black", fill = "white")

    def randomizeAirfoil(self): 
        if self.af.getNumberOfPoints() > 0:
            for i in range(0,self.iterationsPerClick):
                self.af.randomizeGeometry()
                #self.canvas.delete(ALL)
                self.plotAirfoil()
            self.numberOfIterations += self.iterationsPerClick
            labelText = "Number of Iterations: " + str(self.numberOfIterations)
            self.iterationsLabel.config(text = labelText)