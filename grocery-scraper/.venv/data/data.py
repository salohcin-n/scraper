import sqlite3

# This method accepts a scraped object & a table name variable
# It will then create/update the database with the new scraped data.
def saveData(data, table):
    conn = sqlite3.connect('loblaws.db')
    cursor = conn.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL
                    )''')

    try:
        for sublist in data:
            for title, price in sublist:
                try:
                    # Check if the record with the specified name exists
                    cursor.execute(f'SELECT * FROM {table} WHERE name = ?', (title,))
                    existing_record = cursor.fetchone()

                    if existing_record:
                        # If the record exists, update it
                        cursor.execute(f'''UPDATE {table} SET price = ? WHERE name = ?''', (price, title))
                    else:
                        # If the record doesn't exist, insert a new one
                        cursor.execute(f'''INSERT INTO {table} (name, price) VALUES (?, ?)''', (title, price))
                except sqlite3.Error as e:
                    print("Error inserting/updating data:", e)
    except:
        print("Error with data")


    conn.commit()
    conn.close()

# Method to print data to the console
def printData():
    conn = sqlite3.connect('loblaws.db')
    cursor = conn.cursor()

    # This line will delete all data from the table for testing
    # cursor.execute('''DELETE FROM fresh_fruits;''')
    # cursor.execute('''DELETE FROM fresh_vegetables;''')
    # cursor.execute('''DELETE FROM herbs;''')

    try:
        # Execute the SELECT statement
        # cursor.execute('''SELECT * FROM fresh_vegetables''')
        # cursor.execute('''SELECT * FROM fresh_fruits''')

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the retrieved data
        for row in rows:
            print(row)
    except:
        print("Error printing data from database")

    conn.commit()
    conn.close()