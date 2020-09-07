from tkinter import *
from PIL import ImageTk, Image


win = Tk()
win.title("Photo Viewer")

win.iconbitmap('photoIcon.ico')


myImg = ImageTk.PhotoImage(Image.open("Photos/IMG_0118.jpg"))
myLabel = Label(image=myImg)
myLabel.pack()


button_exit = Button(win, text="Exit", command=win.quit)
button_exit.pack()


win.mainloop()