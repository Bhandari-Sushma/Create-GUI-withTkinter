from tkinter import *

win = Tk()
win.title("Check Box")


#var = IntVar()
var = StringVar()


# if var = IntVar()
#checkbox = Checkbutton(win, text="Option1", variable=var)

# if var = StringVar()
checkbox = Checkbutton(win, text="Option1", variable=var, onvalue="on", offvalue="off")
checkbox.deselect()
checkbox.pack()

def show():
    Label(win, text=var.get()).pack()


Button(win, text="Click", command=show).pack()

mainloop()
