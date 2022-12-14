import sqlite3
from sqlite3 import Error

def get_equipment_names():
    connection = None
    try:
        connection = sqlite3.connect('database/berea.db')
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM equipments")
        return [rec[0] for rec in cursor.fetchall()]
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def get_info(name):
    connection = None
    try:
        connection = sqlite3.connect('database/berea.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM equipments WHERE name = (?)", (name,))
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def insert_single(name, location, description, photo_path):
    connection = None
    try:
        connection = sqlite3.connect('database/berea.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO equipments VALUES (?, ?, ?, ?, ?)", (None, name, location, description, photo_path))
        connection.commit()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def insert_multiple(records):
    connection = None
    try:
        connection = sqlite3.connect('database/berea.db')
        cursor = connection.cursor()

        for rec in records:
            cursor.execute("INSERT INTO equipments VALUES (?, ?, ?, ?, ?)", (None, rec[0], rec[1], rec[2], rec[3]))   
        
        connection.commit()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def clear_table():
    connection = None
    try:
        connection = sqlite3.connect('database/berea.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM equipments")
        connection.commit()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    for e in get_equipment_names():
        print(e)