import sqlite3
import uuid

from models.account import Account
from models.user import User

def view_tshirts():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tshirts')
    tshirts = cursor.fetchall()
    conn.close()
    if not tshirts:
        print("No Tshirts in the store for now")
        return None
    return tshirts

def purchase_tshirt(user_id, tshirt_id):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT price FROM tshirts WHERE id=?', (tshirt_id,))
    tshirt = cursor.fetchone()
    if not tshirt:
        print("T-shirt not found.")
        return
    
    price = tshirt[0]
    
    cursor.execute('SELECT balance FROM accounts WHERE user_id=?', (user_id,))
    account = cursor.fetchone()
    if not account or account[0] < price:
        print("Insufficient balance.")
        return
    
    new_balance = account[0] - price
    cursor.execute('UPDATE accounts SET balance=? WHERE user_id=?', (new_balance, user_id))
    conn.commit()
    conn.close()
    print("Purchase successful.")

def rate_tshirt(tshirt_id, rating):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tshirts SET rating=? WHERE id=?', (rating, tshirt_id))
    conn.commit()
    conn.close()
    print("Rating submitted.")


def create_user(name,email,password,dob):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name,email,password,dob) VALUES (?,?,?,?)',(name,email,password,dob))
    user_id =  cursor.lastrowid

    account_number = str(uuid.uuid4())
    initial_balance = 5000.00
    cursor.execute('INSERT INTO accounts (user_id, account_number, balance) VALUES (?, ?, ?)', (user_id, account_number, initial_balance))

    # Create User and Account objects
    user = User(name, email, password, dob)
    account = Account(user_id, account_number, initial_balance)
    user.set_account(account)

    conn.commit()
    conn.close()
    print("User created!")