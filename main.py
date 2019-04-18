from tkinter import *

root = Tk()

topFrame = Frame(root)              #init container
topFrame.pack()                     #place in window
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text = "File", fg = "black")
button2 = Button(topFrame, text = "Settings", fg = "black")
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()