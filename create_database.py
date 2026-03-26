import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Create users table
c.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Create patients table
c.execute("""
CREATE TABLE patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    glucose REAL,
    bmi REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")