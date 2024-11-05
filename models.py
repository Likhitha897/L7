# models.py
import sqlite3

def add_flavor(name, season):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Flavors (name, season) VALUES (?, ?)", (name, season))
    connection.commit()
    connection.close()

def get_all_flavors():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Flavors")
    flavors = cursor.fetchall()
    connection.close()
    return flavors
