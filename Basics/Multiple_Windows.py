from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Main window")


def open():
    global my_img
    second = Toplevel()
    second.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("Photos/img1.jpg"))
    Label(second, image=my_img).pack()
    Button(second, text="Close", command=second.destroy).pack()


Button(win, text="Open new window", command=open).pack()

mainloop()
