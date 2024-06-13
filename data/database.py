import sqlite3

def initialize_db():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        dob TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        account_number TEXT UNIQUE NOT NULL,
                        balance REAL NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tshirts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        color TEXT NOT NULL,
                        size TEXT NOT NULL,
                        price REAL NOT NULL,
                        category TEXT NOT NULL,
                        rating REAL)''')
    
    # cursor.execute('''INSERT INTO admins (
    #                     username,
    #                     password ) VALUES ('admin', 'password')
    #                     ''')

    conn.commit()
    conn.close()
