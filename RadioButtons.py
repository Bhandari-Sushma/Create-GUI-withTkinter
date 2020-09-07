from tkinter import *

win = Tk()
win.title("Radio Buttons")

#r = IntVar()        # tkinter variables
#r.set("1")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

# tkinter variable
pizzaTopping = StringVar()
pizzaTopping.set("Pepperoni")


# looping is much cleaner than writing 4 lines of code
for text, mode in MODES:
    Radiobutton(win, text=text, variable=pizzaTopping, value=mode).pack(anchor=W)   # anchor -> left alighned i.e. on west side


def clicked(value):
    mylabel = Label(win, text=value)
    mylabel.pack()

#Radiobutton(win, text="option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(win, text="option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Button(win, text="Click me!!", command=lambda :clicked(r.get())).pack()


mainloop()