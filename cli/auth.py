import sqlite3

def authenticate_user(email, password):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def authenticate_admin(username, password):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admins WHERE username=? AND password=?', (username, password))
    admin = cursor.fetchone()
    conn.close()
    return admin
