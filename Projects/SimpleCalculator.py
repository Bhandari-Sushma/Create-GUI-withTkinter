from tkinter import *

win = Tk()
win.title("Simple Calculator")

inputs = Entry(win, width=35, borderwidth=5)
inputs.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = inputs.get()
    inputs.delete(0, END)
    inputs.insert(0, str(current) + str(number))


def button_clear():
    inputs.delete(0, END)


def button_add():
    f_num = inputs.get()
    global first_number
    global math
    math = "addition"
    first_number = int(f_num)
    inputs.delete(0, END)


def button_subtract():
    f_num = inputs.get()
    global first_number
    global math
    math = "subtraction"
    first_number = int(f_num)
    inputs.delete(0, END)


def button_multiply():
    f_num = inputs.get()
    global first_number
    global math
    math = "multiplication"
    first_number = int(f_num)
    inputs.delete(0, END)


def button_divide():
    f_num = inputs.get()
    global first_number
    global math
    math = "division"
    first_number = int(f_num)
    inputs.delete(0, END)


def button_equal():
    second_number = int(inputs.get())
    inputs.delete(0, END)

    if math == "addition":
        inputs.insert(0, first_number + second_number)
    if math == "subtraction":
        inputs.insert(0, first_number - second_number)
    if math == "multiplication":
        inputs.insert(0, first_number * second_number)
    if math == "division":
        inputs.insert(0, first_number / second_number)


# Define Buttons

button_1 = Button(win, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_add = Button(win, text="+", padx=20, pady=20, command=button_add)
button_equal = Button(win, text="=", padx=20, pady=20, command=button_equal)
button_clear = Button(win, text="C", padx=20, pady=20, command=button_clear)
button_subtract = Button(win, text="- ", padx=20, pady=20, command=button_subtract)
button_multiply = Button(win, text="x", padx=20, pady=20, command=button_multiply)
button_divide = Button(win, text="/", padx=20, pady=20, command=button_divide)

# Put the buttons on the screen

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)


button_0.grid(row=4, column=0)
button_divide.grid(row=4, column=1)
button_multiply.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

win.mainloop()
