# database.py
import sqlite3

def init_db():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    # Create Seasonal Flavors table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            season TEXT NOT NULL
        )
    """)
    # Create Ingredients table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    # Create Customer Feedback table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CustomerFeedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suggestion TEXT,
            allergy TEXT
        )
    """)
    connection.commit()
    connection.close()

# Run this script directly to initialize the database
if __name__ == "__main__":
    init_db()
    print("Database initialized.")
