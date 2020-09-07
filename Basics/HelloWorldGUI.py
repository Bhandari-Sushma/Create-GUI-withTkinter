from tkinter import *

root = Tk()

root.title("First GUI")

# create input box
input = Entry(root, width=30)
input.pack()
input.insert(0, "Enter you name:")  # default input display


# function to be executed when the button is clicked
def click():
    hello = 'Hello ! ' + input.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# Button
mybutton = Button(root, text="Enter", command=click)
mybutton.pack()

root.mainloop()
