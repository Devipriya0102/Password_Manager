import sqlite3
import os

DB_FOLDER = os.path.join(os.path.dirname(__file__), "database")
DB_PATH = os.path.join(DB_FOLDER, "passwords.db")

# Ensure database folder exists
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)  # Create "database/" folder if missing
# Database connection
def connect_db():
    conn = sqlite3.connect("database/passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

# Add a new password
def add_password(website, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
                   (website, username, password))
    conn.commit()
    conn.close()

# Retrieve all passwords
def get_passwords():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    data = cursor.fetchall()
    conn.close()
    return data

# Delete a password entry
def delete_password(password_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
    conn.commit()
    conn.close()
