from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


win = Tk()
win.title("Charts and Graphs")
win.geometry("400x600")


def graph():
    house_prices = np.random.normal(2000000, 25000, 5000)
    plt.hist(house_prices, 50)
    # (plt.piechart...)
    plt.show()


my_button = Button(win, text="Graph it!", command=graph)
my_button.pack()


win.mainloop()


