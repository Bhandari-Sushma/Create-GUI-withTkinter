from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Message Box")


# Various functions of messagebox : showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def Popup():
    response = messagebox.askyesnocancel("This is my Popup", "HelloWorld!")
    # Label(win, text=response).pack()
    if response == 1:
        Label(win, text="You clicked 'Yes'!").pack()
    elif response == 0:
        Label(win, text="You clicked 'No'!").pack()
    else:
        Label(win, text="You clicked 'Cancel'!").pack()


Button(win, text="Popup", command=Popup).pack()

mainloop()
