import sqlite3

def add_tshirt(name, color, size, price, category):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tshirts (name, color, size, price, category) VALUES (?, ?, ?, ?, ?)', 
                   (name, color, size, price, category))
    conn.commit()
    conn.close()
    print("T-shirt added.")

def update_tshirt(tshirt_id, name, color, size, price, category):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE tshirts SET name=?, color=?, size=?, price=?, category=? WHERE id=?''', 
                   (name, color, size, price, category, tshirt_id))
    conn.commit()
    conn.close()
    print("T-shirt updated.")

def delete_tshirt(tshirt_id):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tshirts WHERE id=?', (tshirt_id,))
    conn.commit()
    conn.close()
    print("T-shirt deleted.")

def view_all_tshirts():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tshirts')
    tshirts = cursor.fetchall()
    conn.close()
    return tshirts
