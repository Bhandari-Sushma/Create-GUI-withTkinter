from tkinter import *
import mysql.connector

win = Tk()
win.title('CRM Database')
win.geometry("400x400")


# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Himalaya@1b",
    database = "myorganization"
)

# Create a cursor and intialize it
my_cursor = mydb.cursor()


# Create database
#my_cursor.execute("CREATE DATABASE myorganization")

# Delete database
#my_cursor.execute("DROP DATABASE myorganization")



'''
# Create a table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
first_name VARCHAR(255), 
last_name VARCHAR(255), 
zip_code INT(10), 
price_paid DECIMAL(10, 2), 
user_id INT AUTO_INCREMENT PRIMARY KEY)""")
'''

# Delete Table
#my_cursor.execute("DROP TABLE customers")


'''
# Add columns to the table
my_cursor.execute("""ALTER TABLE customers ADD(
                    email VARCHAR(255),
                    address_1 VARCHAR(255),
                    city VARCHAR(50),
                    state VARCHAR(50),
                    country VARCHAR(255),
                    phone_no VARCHAR(255),
                    payment_method VARCHAR(50),
                    discount_code VARCHAR(255)                     
                    )""")
'''



# Show table content
my_cursor.execute("SELECT * from customers")
for items in my_cursor.description:
    print(items)


# Function to add customers to the database
def add_customers():
    sql_command = ""
    values = ""
    my_cursor.execute(sql_command, values)




win.mainloop()