from tkinter import *
import sqlite3


win = Tk()
win.title("Database")

# create a database (if already doesnot exist) or connect to the database (if already exist)
conn = sqlite3.connect("address_book.db")

# create cursor
cur = conn.cursor()


# Create a table
cur.execute(""" CREATE TABLE addresses(
                first_name text, 
                last_name  text, 
                address text, 
                city text,
                state text,
                zip_code integer)
""")

# commit to changes
conn.commit()

# close the connection
conn.close()

# start the GUI
win.mainloop()