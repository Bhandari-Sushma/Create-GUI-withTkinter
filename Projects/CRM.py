from tkinter import *
import mysql.connector
import csv

win = Tk()
win.title('CRM Database')
win.geometry("500x700")

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


# Write to CSV function
def write_to_csv(results):
    with open('customers.csv', 'w', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for records in results:
            w.writerow(records)


def search_customer():
    search_customers = Tk()
    search_customers.title('Search Customers')
    search_customers.geometry("800x600")

    def search_now():
        searched = search_box.get()
        sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record not found ....."

        searched_label = Label(search_customers, text=result)
        searched_label.grid(row=2, column=0, columnspan=2, padx=10)


    # Entry box to search for customers
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    search_box_label = Label(search_customers, text="Search By Last Name:")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    # Entry box search Button
    search_button = Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10, pady=10)




# Function to list customers
def list_customers():
    customers_list_query = Tk()
    customers_list_query.title('Customers List')
    customers_list_query.geometry("800x600")

    # Query the database
    my_cursor.execute("SELECT * FROM customers")
    results = my_cursor.fetchall()

    for index, x in enumerate(results):
        num = 0
        for y in x:
            loopup_label = Label(customers_list_query, text=y)
            loopup_label.grid(row=index, column=num)
            num += 1

    csv_button = Button(customers_list_query, text="Save to Excel", command=lambda: write_to_csv(results))
    csv_button.grid(row=len(results)+1, column=0)


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
add_submit_button.grid(row=14, column=0, padx=10, pady=10, ipadx=30)

clear_fields_button = Button(win, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1, padx=10, pady=10, ipadx=30)

customers_list_button = Button(win, text="List Customers", command=list_customers)
customers_list_button.grid(row=15, column=0, sticky=W, padx=10)

    # Search customers
search_customers_buttons = Button(win, text="Search Customers", command=search_customer)
search_customers_buttons.grid(row=15, column=1, sticky=W, padx=10)


win.mainloop()
