from tkinter import *
import sqlite3

win = Tk()
win.title("Database")
win.geometry("400x400")

# create a database (if already doesnot exist) or connect to the database (if already exist)
conn = sqlite3.connect("address_book.db")

# create cursor
cur = conn.cursor()


# Create function to delete a record
def delete():
    # create a database (if already doesnot exist) or connect to the database (if already exist)
    conn = sqlite3.connect('address_book.db')

    # create cursor
    cur = conn.cursor()

    # delete a record
    cur.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # commit to changes
    conn.commit()

    # close the connection
    conn.close()


# Create submit function for database
def submit():
    # create a database (if already doesnot exist) or connect to the database (if already exist)
    conn = sqlite3.connect('address_book.db')

    # create cursor
    cur = conn.cursor()

    # Insert into table
    cur.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zip_code)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zip_code': zip_code.get()
                }
                )

    # commit to changes
    conn.commit()

    # close the connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)


# Create query function
def query():
    # create a database (if already doesnot exist) or connect to the database (if already exist)
    conn = sqlite3.connect("address_book.db")

    # create cursor
    cur = conn.cursor()

    # Query the database
    cur.execute("SELECT *, oid from addresses")
    records = cur.fetchall()  # fecthone, fetchmany(num)
    # print(records)

    # loop through results
    print_record = ''
    for record in records:
        print_record += str(record) + "\n"

    query_lable = Label(win, text=print_record)
    query_lable.grid(row=14, column=0, columnspan=2)

    # commit to changes
    conn.commit()

    # close the connection
    conn.close()


# create text boxes

f_name = Entry(win, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(win, width=30)
l_name.grid(row=1, column=1)
address = Entry(win, width=30)
address.grid(row=2, column=1)
city = Entry(win, width=30)
city.grid(row=3, column=1)
state = Entry(win, width=30)
state.grid(row=4, column=1)
zip_code = Entry(win, width=30)
zip_code.grid(row=5, column=1)

delete_box = Entry(win, width=30)
delete_box.grid(row=10, column=1)

# Create text box Lables
f_name_label = Label(win, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(win, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(win, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(win, text="City")
city_label.grid(row=3, column=0)
state_label = Label(win, text="State")
state_label.grid(row=4, column=0)
zip_code_label = Label(win, text="Zipcode")
zip_code_label.grid(row=5, column=0)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.grid(row=10, column=0)
# Create submit button
submit_button = Button(win, text="Add record to database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=102)

# Create a query button
query_btn = Button(win, text="Show Recods", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a delete button
query_btn = Button(win, text="Delete Recod", command=delete)
query_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# commit to changes
conn.commit()

# close the connection
conn.close()

# start the GUI
win.mainloop()
