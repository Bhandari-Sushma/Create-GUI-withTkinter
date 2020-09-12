from tkinter import *
import mysql.connector

win = Tk()
win.title('CRM Database')
win.geometry("600x800")

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Himalaya@1b",
    database="myorganization"
)

# Create a cursor and intialize it
my_cursor = mydb.cursor()


# Function for clear fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zip_code_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


# Function to add customers to the database
def add_customers():
    sql_command = "INSERT INTO customers (first_name, last_name, zip_code, price_paid, email, address_1, address_2, city, state, country, phone_no, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zip_code_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(),
              state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    # Commit the changes to database
    mydb.commit()

    # clear the fields
    clear_fields()


# Create a lable
title_label = Label(win, text="MyOrganization Database", font=("Helvetica", 16))
title_label.grid(row=0, column=1, columnspan=2, pady='10')

# Create Main form to enter customer data
first_name_label = Label(win, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(win, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(win, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(win, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(win, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(win, text="State").grid(row=6, column=0, sticky=W, padx=10)
zip_code_label = Label(win, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(win, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(win, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(win, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(win, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(win, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(win, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

# Create Entry BOxes
first_name_box = Entry(win)
first_name_box.grid(row=1, column=1, pady=10)
last_name_box = Entry(win)
last_name_box.grid(row=2, column=1, pady=10)
address1_box = Entry(win)
address1_box.grid(row=3, column=1, pady=10)
address2_box = Entry(win)
address2_box.grid(row=4, column=1, pady=10)
city_box = Entry(win)
city_box.grid(row=5, column=1, pady=10)
state_box = Entry(win)
state_box.grid(row=6, column=1, pady=10)
zip_code_box = Entry(win)
zip_code_box.grid(row=7, column=1, pady=10)
country_box = Entry(win)
country_box.grid(row=8, column=1, pady=10)
phone_box = Entry(win)
phone_box.grid(row=9, column=1, pady=10)
email_box = Entry(win)
email_box.grid(row=10, column=1, pady=10)
payment_method_box = Entry(win)
payment_method_box.grid(row=11, column=1, pady=10)
discount_code_box = Entry(win)
discount_code_box.grid(row=12, column=1, pady=10)
price_paid_box = Entry(win)
price_paid_box.grid(row=13, column=1, pady=10)

# Create Buttons
add_submit_button = Button(win, text="SUBMIT", command=add_customers)
add_submit_button.grid(row=15, column=0, padx=10, pady=10, ipadx=30)

clear_fields_button = Button(win, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15, column=1, padx=10, pady=10, ipadx=30)

win.mainloop()
