import sqlite3

# This method accepts a scraped object & a table name variable
# It will then create/update the database with the new scraped data.
def saveVeggieData(data, table):
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
                    cursor.execute(f'''INSERT OR REPLACE INTO {table} (name, price)
                                                            values (?, ?)''', (title, price))
                except sqlite3.Error as e:
                    print("Error inserting data", e)
    except:
        print("Error with data")


    conn.commit()
    conn.close()

# Method to print data to the console
def printData():
    conn = sqlite3.connect('loblaws.db')
    cursor = conn.cursor()

    # This line will delete all data from the table for testing
    # cursor.execute('''DELETE FROM fresh_vegetables;''')

    try:
        # Execute the SELECT statement
        cursor.execute('''SELECT * FROM fresh_vegetables''')

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the retrieved data
        for row in rows:
            print(row)
    except:
        print("Error printing data from database")

    conn.commit()
    conn.close()