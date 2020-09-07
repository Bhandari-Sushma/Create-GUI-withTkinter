from tkinter import *


win = Tk()
win.title("SLIDERS")
win.geometry("600x600")

vertical = Scale(win, from_=0, to=100)
vertical.pack()

horizontal = Scale(win, from_=0, to=600, orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_lable = Label(win, text=horizontal.get()).pack()
    win.geometry(str(horizontal.get()) + "x600")


my_button = Button(win, text="Click", command=slide).pack()

mainloop()