import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Function to insert data into the table
def insert_data():
    users_name = name_entry.get()
    users_phonenumber = phonenumber_entry.get()
    users_id = id_entry.get()
    users_birth_day = dayField.get()
    users_birth_month = monthField.get()
    users_birth_year = yearField.get() 
    users_age = age_year_entry.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cafe membership"
    )
    cursor = conn.cursor()

    # Corrected the INSERT INTO syntax and removed quotes from the data variable
    insert_query = "INSERT INTO users (users_name, users_phonenumber, users_id, users_birth_day, users_birth_month, users_birth_year, users_age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (users_name, users_phonenumber, users_id, users_birth_day, users_birth_month, users_birth_year, users_age)

    cursor.execute(insert_query, data)

    conn.commit()
    conn.close()
	
def calculate_age():
    # Extract values from the respective entry boxes
    birth_day = int(dayField.get())
    birth_month = int(monthField.get())
    birth_year = int(yearField.get())

    given_day = int(current_day.get())
    given_month = int(current_month.get())
    given_year = int(current_year.get())

    # If birth date is greater than given birth_month, adjust the values
    if birth_day > given_day:
        given_month -= 1
        given_day += 30  # Assuming a 30-day month to simplify

    if birth_month > given_month:
        given_year -= 1
        given_month += 12

    # Calculate day, month, year
    calculated_day = given_day - birth_day
    calculated_month = given_month - birth_month
    calculated_year = given_year - birth_year

    # Insert the calculated year into the entry box
    age_year_entry.insert(10, str(calculated_year))


# Tkinter GUI
root = tk.Tk()
root.title("MySQL Database with Tkinter")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

label_phonenumber = tk.Label(root, text="Phone number:")
label_phonenumber.grid(row=1, column=0)
phonenumber_entry = tk.Entry(root)
phonenumber_entry.grid(row=1, column=1)

label_id = tk.Label(root, text="Id:")
label_id.grid(row=2, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1)

# Date of birth
birth_date = tk.Label(root, text="Birth Day", font=('Times New Roman', 14, 'bold'))
birth_date.grid(row=3, column=0)
birth_month = tk.Label(root, text="Birth Month", font=('Times New Roman', 14, 'bold'))
birth_month.grid(row=3, column=1)
birth_year = tk.Label(root, text="Birth Year", font=('Times New Roman', 14, 'bold'))
birth_year.grid(row=3, column=2)

# Create a text entry box for filling or typing the information(dob). 
dayField = tk.Entry(root)
dayField.grid(row=4, column=0)
monthField = tk.Entry(root)
monthField.grid(row=4, column=1)
yearField = tk.Entry(root)
yearField.grid(row=4, column=2)

# Current Year
curr_day = tk.Label(root, text= "Current Day", font=('Times New Roman',14, 'bold'))
curr_day.grid(row=5,column=0)
curr_month = tk.Label(root, text= "Current Month", font=('Times New Roman',14, 'bold'))
curr_month.grid(row=5, column=1)
curr_year = tk.Label(root, text= "Current Year", font=('Times New Roman',14, 'bold'))
curr_year.grid(row=5, column=2)

# Create a text entry box for filling or typing the information(current year). 
current_day = tk.Entry(root)
current_day.grid(row=6, column=0)
current_month = tk.Entry(root)
current_month.grid(row=6, column=1)
current_year = tk.Entry(root)
current_year.grid(row=6, column=2)	

# Age results
resultantAge = tk.Button(root, text = "Age", command = calculate_age, padx=25, pady=5)
resultantAge.grid(row=8, column=1, sticky= "news")

age_year = tk.Label(root, text= "Age:", font=('Times New Roman',14))
age_year.grid(row=7, column=0)
age_year_entry = tk.Entry(root)
age_year_entry.grid(row=7, column=1)

for widget in root.winfo_children():
    widget.grid(padx=10, pady=5)

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=9, column=1, sticky="news")

root.mainloop()