from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Photo Viewer")

win.iconbitmap('photoIcon.ico')

myImg1 = ImageTk.PhotoImage(Image.open("../Photos/img1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("../Photos/img2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("../Photos/img3.jpg"))

image_list = [myImg1, myImg2, myImg3]

my_label = Label(image=myImg1, padx=15, pady=15)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(win, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(win, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(win, text="<<", command=lambda: backward(image_num - 1))

    if image_num == 3:
        button_forward = Button(win, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column=1)

    status = Label(win, text="Image " + str(image_num) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=6, column=0, columnspan=3, sticky=W + E)


def backward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(win, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(win, text="<<", command=lambda: backward(image_num - 1))

    if image_num == 1:
        button_back = Button(win, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=4, column=0)
    button_forward.grid(row=4, column=1)

    status = Label(win, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=6, column=0, columnspan=3, sticky=W + E)


button_back = Button(win, text="<<", command=backward, state=DISABLED)
button_exit = Button(win, text="Exit", command=win.quit)
button_forward = Button(win, text=">>", command=lambda: forward(2))

button_back.grid(row=4, column=0)
button_forward.grid(row=4, column=1)
button_exit.grid(row=4, column=2, pady=10)
status.grid(row=6, column=0, columnspan=3, sticky=W+E)

win.mainloop()
