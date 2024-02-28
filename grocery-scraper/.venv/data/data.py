import sqlite3

def saveVeggieData(data):
    conn = sqlite3.connect('loblaws.db')
    cursor.execute('''CREATE TABLE IF NOT EXISTS fresh_vegetables (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL
                    )''')

    # Extracting data from the DataFrame
    veggie_data = [(row['Name'], row['Price']) for index, row in data.iterrows()]

    # Insert data into the table
    cursor.executemany("INSERT INTO fresh_vegetables (name, price) VALUES (?, ?)", veggie_data)

    conn.commit()
    conn.close()