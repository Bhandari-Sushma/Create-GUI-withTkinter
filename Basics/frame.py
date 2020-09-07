from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("Frame")

frame = LabelFrame(win, text="This is my frame...", padx=50, pady=50)
frame.pack()

b = Button(frame, text="Click")
b.pack()

win.mainloop()
