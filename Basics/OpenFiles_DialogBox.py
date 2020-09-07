from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


win = Tk()
win.title("Open File Dialogue")


def open():
    global my_img
    filename = filedialog.askopenfilename(initialdir="Photos", title="Select a file", filetypes=(("All", "*.*"),("JPG files", "*.jpg")))
    #Label(win, text=filename).pack()   # just display the file path
    my_img = ImageTk.PhotoImage(Image.open(filename))
    Label(image=my_img).pack()


Button(win, text="Browse", command=open).pack()

mainloop()