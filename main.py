from tkinter import *
import tkinter.messagebox
import os

os.system('cls')                                                                                    #clear console


class mainWindow:                                                                                   #Main window for program

    def __init__(self, master):
        topFrame = Frame(master)
        topFrame.pack(side = TOP)
        bottomFrame = Frame(master, height = 200, width = 400)
        bottomFrame.pack(side = BOTTOM)

        #self.fileButton = Button(topFrame, text = "File", fg = "Black")
        #self.fileButton.grid(row = 0, column = 0, sticky = W)
        #self.fileButton.bind("<Button-1>", self.test)

        #self.settingsButton = Button(topFrame, text = "Settings", fg = "black")
        #self.settingsButton.grid(row = 0, column = 1, sticky = W)
        #self.settingsButton.bind("<Button-1>", self.test)

        self.menu = Menu(topFrame)                                                                  #Menu across top of window
        master.config(menu=self.menu)

        self.fileSubMenu = Menu(self.menu, tearoff = False)
        self.menu.add_cascade(label = "File", menu = self.fileSubMenu)
        self.fileSubMenu.add_command(label = "Settings", command = self.openSettings)
        self.fileSubMenu.add_separator()
        self.fileSubMenu.add_command(label = "Quit", command = self.quit)

    def test(self):
        print("test")

    def quit(self):
        answer = tkinter.messagebox.askquestion("Quit?", "Are you sure you want to quit?")
        
        if answer == "yes":
            root.destroy()

    def openSettings(self):
        settings = Toplevel()
        settings.title("Settings Menu")
        self.closeSettings = Button(settings, text = "Close", command = settings.destroy)
        self.closeSettings.pack()

root = Tk()
window = mainWindow(root)
root.mainloop()