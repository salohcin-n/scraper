import sqlite3

def saveVeggieData(data):
    conn = sqlite3.connect('loblaws.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS fresh_vegetables (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL
                    )''')

    try:
        for sublist in data:
            for title, price in sublist:
                try:
                    cursor.execute('''INSERT INTO fresh_vegetables (name, price)
                                                            values (?, ?)''', (title, price))
                except sqlite3.Error as e:
                    print("Error inserting data", e)
    except:
        print("Error with data")

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