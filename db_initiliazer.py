import sqlite3

# connect to the database (create it if not existing already)
connection = sqlite3.connect('database/berea.db')

# a cursor object to run queries
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE equipments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT,
        photo TEXT
    )
""")

# commit the changes
connection.commit()

records = [
    (None, 'Apple', 'Not available', 'Delicious', 'Not available'),
    (None, 'Orange', 'Not available', 'Tasty', 'Not available'),
    (None, 'Banana', 'Not available', 'Fine', 'Not available'),
    (None, 'Pineapple', 'Not available', 'Sour', 'Not available'),
]

cursor.executemany("INSERT INTO equipments VALUES (?, ?, ?, ?, ?)", records)
connection.commit()

connection.close()