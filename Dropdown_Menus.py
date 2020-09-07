from tkinter import *

win = Tk()
win.title("Dropdown menu")
win.geometry("400x400")


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

selected = StringVar()
selected.set(options[0])

dropdown = OptionMenu(win, selected, *options)
dropdown.pack()

def show():
    Label(win, text=selected.get()).pack()


Button(win, text="Show Selection", command=show).pack()

mainloop()