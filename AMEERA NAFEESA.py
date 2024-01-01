import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="luxury_car_rental"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    customer_name = customer_name_entry.get()
    customer_phone = customer_phone_entry.get()
    car_model = selected_car_var.get()
    day = int(duration_day.get())

    # The price below is to define the value from your selections
    prices = {
        "Car A": 1200,
        "Car B": 1600,
        "Car C": 1400,
        "Car D": 2000,
    }

    # Calculate the total price. This will be derived from your selection (Selected Car, Duration Day).
    total_price = prices.get(car_model, 0) * day

    # To insert your Data to your database, As for this example, you have 3 attributes. (2 Attributes from your selection (Selected cars, Duration Day) and another attributes that derived from your attributes (price))
    sql = "INSERT INTO `cust_info` (cust_name, cust_phone, car_model, rental_duration, rental_price) VALUES (%s, %s, %s, %s, %s)"
    val = (customer_name, customer_phone, car_model, day, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python.
    output_label.config(text=f"Customer: {customer_name}\nPhone: {customer_phone}\nCar: {car_model}, Duration: {day} days, Total Price: RM{total_price}")

# Your Main window, You need to have the title, geometry
root = tk.Tk()
root.title("Car Rental")
root.geometry('500x800')

# Set background color to black
root.configure(bg='brown')

# Page Title
label = tk.Label(root, text='Calculate Your Car Model Price', font=("Times New Roman",14, "bold"), fg='tan', bg='brown')
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=13, width=45, font=("Times New Roman",14,), fg= 'beige', bg='brown')
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "Car Model & Prices:\n\n")
prices_text.insert(tk.END, "Car A: Mercedez Benz S Class\nPrice: RM1200\n\n")
prices_text.insert(tk.END, "Car B: BMW 7 Series \nPrice: RM1600\n\n")
prices_text.insert(tk.END, "Car C: Audi R8\nPrice: RM1400\n\n")
prices_text.insert(tk.END, "Car D: Toyota Vellfire \nPrice: RM2000\n\n")
prices_text.configure(state='disabled')

# Customer Name Entry
customer_name_label = tk.Label(root, text="Customer Name:", font= ("Times New Roman", 14), fg='beige', bg='brown')
customer_name_label.pack()
customer_name_entry = tk.Entry(root)
customer_name_entry.pack()

# Customer Phone Entry
customer_phone_label = tk.Label(root, text="Customer Phone:", font= ("Times New Roman",14,), fg='beige', bg='brown')
customer_phone_label.pack()
customer_phone_entry = tk.Entry(root)
customer_phone_entry.pack()

# Car Type Dropdown (Label)
car_label = tk.Label(root, text="Choose Your Car:", font=("Times New Roman",14, ), fg='beige', bg='brown')
car_label.pack()

# Car Type Dropdown
selected_car_var = tk.StringVar(root)
selected_car_var.set("Select Your Car")  # Default value before your selection
car_dropdown = tk.OptionMenu(root, selected_car_var, "Car A", "Car B", "Car C", "Car D")
car_dropdown.pack(pady=10)

# Duration Entry
day_label = tk.Label(root, text="Day:", font=("Times New Roman",14), fg='beige', bg='brown')
day_label.pack()
duration_day= tk.Entry(root)
duration_day.pack()

# Save Button
save_button = tk.Button(root, text="Calculate", command=collect_data, fg='beige', bg='brown')
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Car Price', font=("Times New Romans",12), fg='beige', bg='brown')
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="", fg='beige', bg='brown')
output_label.pack()

root.mainloop()

