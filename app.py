import mysql.connector

# Establish a database connection
conn = mysql.connector.connect(
    host="localhost",        # or the address where your MySQL is hosted
    user="root",             # MySQL username
    password="root", # MySQL password
    database="ExpenseTracker"
)
cursor = conn.cursor()

# Function to add an expense with user inputs
def add_expense():
    # Prompt user for input
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense (e.g., Food, Transport): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return
    description = input("Enter a description of the expense: ")

    # Insert the expense into the database
    query = "INSERT INTO Expenses (date, category, amount, description) VALUES (%s, %s, %s, %s)"
    data = (date, category, amount, description)
    cursor.execute(query, data)
    conn.commit()
    print("Expense added successfully!")

# Main loop to allow multiple entries
while True:
     print("\nPersonal Expense Tracker")
     print("1. Add Expense")
     print("2. Exit")

     choice = input("Enter your choice: ")

     if choice == "1":
        add_expense()
     elif choice == "2":
        break
     else:
        print("Invalid choice, please try again.")

# Close the connection
conn.close()

