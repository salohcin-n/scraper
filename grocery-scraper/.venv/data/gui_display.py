import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import font  # Import the font module

# Function to connect to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to autosize columns
def autosize_columns(tree, col_name):
    tree.update_idletasks()  # Update the UI so the widths are current
    width = font.Font().measure(col_name)  # Get the width of the column header
    for row in tree.get_children():
        item_width = font.Font().measure(tree.set(row, col_name))
        width = max(width, item_width)  # Set the new width to the larger of the two
    tree.column(col_name, width=width)  # Set the column width to the max width found

# Function to execute a query and return the results
def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

# Function to search for an item by name
def search_item(tree, query):
    # Remove all current items in the tree
    for i in tree.get_children():
        tree.delete(i)
    # Re-populate the tree with search results
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT name, price, type FROM produce WHERE name LIKE ?", ('%' + query + '%',))
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=row)

# Function to create the GUI window
def create_gui(db_file):
    # Create the main window
    root = tk.Tk()
    root.title("Grocery Price Data")

    # Create a frame for the Treeview and scrollbar
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(frame, columns=('Item', 'Price', 'Type'), show='headings')
    tree.heading('Item', text='Item')
    tree.heading('Price', text='Price')
    tree.heading('Type', text='Type')

    # Create a vertical scrollbar
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar into the frame
    tree.pack(side='left', expand=True, fill='both')
    vsb.pack(side='right', fill='y')

    # Search entry and button
    search_var = tk.StringVar()
    search_entry = tk.Entry(root, textvariable=search_var)
    search_entry.pack(side='top', padx=10, pady=10)
    search_button = tk.Button(root, text="Search", command=lambda: search_item(tree, search_var.get()))
    search_button.pack(side='top', padx=10, pady=10)

    # Connect to the database and retrieve the data
    conn = create_connection(db_file)
    if conn is not None:
        data = execute_query(conn, "SELECT name, price, type FROM produce")
        for row in data:
            tree.insert('', tk.END, values=row)

        # Autosize columns
        autosize_columns(tree, 'Item')
        autosize_columns(tree, 'Price')
        autosize_columns(tree, 'Type')

    # Start the GUI event loop
    root.mainloop()

# Replace 'your_database.db' with the path to your actual database file
# database = r'C:\GitHub\scraper\grocery-scraper\.venv\loblaws.db'
# create_gui(database)