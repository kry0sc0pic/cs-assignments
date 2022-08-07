"""
Stock Management system.
Consider the following table structure istock
Write the commands to :
1.create connection between Python and mysql
2.create database stock.
3. activate database stock
4. create table istock where ino is primary key
5. create menu driven program to do the following.
    1. additem(): To insert records
    2. buyitem(): To update quantity on purchase (add if item exists otherwise display proper
    message)accepting itemno from the user
    3. issueitem():To update quantity on issue(subtract if item exists otherwise display proper message)
    accepting itemno from the user
    4.delete itemno(): To delete the itemno from table
    5. displayall(): To display all records
    6. searchonitemno(): To display the items after accepting item number from user
    7. searchonitemname():To display the items after accepting item name from user
    8. searchissue_purchaselist(): accept transaction type ‘P’ or ‘I’ and display details
    9.quit()
"""

import mysql.connector as sql
#1
conn = sql.connect(host="localhost", user="root", password="",)
cursor = conn.cursor()
# 2
cursor.execute("CREATE DATABASE stock")
# 3
cursor.execute("USE stock")
# 4
cursor.execute("CREATE TABLE istock(INO INT PRIMARY KEY, INAMe VARCHAR(20), quantity INT, price INT, )")
cursor.commit()

# 5.1
def additem():
    global cursor
    global conn
    ino = int(input("Enter item number: "))
    itemname = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price: "))
    cursor.execute("INSERT INTO istock(ino, itemname, quantity, price) VALUES(%s, %s, %s, %s)", (ino, itemname, quantity, price))
    conn.commit()
    conn.close()
    print("Item added successfully")
    return

# 5.2
def buyitem():
    global cursor
    global conn
    ino = int(input("Enter item number: "))
    cursor.execute("SELECT * FROM istock WHERE ino = %s", (ino,))
    row = cursor.fetchone()
    if row is None:
        print("Item not found")
    else:
        quantity = int(input("Enter quantity: "))
        cursor.execute("UPDATE istock SET quantity = quantity + %s WHERE ino = %s", (quantity, ino))
        conn.commit()
        print("Item updated successfully")
    return

# 5.3
def issueitem():
    global cursor
    global conn
    ino = int(input("Enter item number: "))
    cursor.execute("SELECT * FROM istock WHERE ino = %s", (ino,))
    row = cursor.fetchone()
    if row is None:
        print("Item not found")
    else:
        quantity = int(input("Enter quantity: "))
        cursor.execute("UPDATE istock SET quantity = quantity - %s WHERE ino = %s", (quantity, ino))
        conn.commit()
        print("Item updated successfully")
    return

# 5.4
def deleteitemno():
    global cursor
    global conn
    ino = int(input("Enter item number: "))
    cursor.execute("DELETE FROM istock WHERE ino = %s", (ino,))
    conn.commit()
    print("Item deleted successfully")
    return

# 5.5
def displayall():
    global cursor
    global conn
    cursor.execute("SELECT * FROM istock")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return

# 5.6
def searchonitemno():
    global cursor
    global conn
    ino = int(input("Enter item number: "))
    cursor.execute("SELECT * FROM istock WHERE ino = %s", (ino,))
    row = cursor.fetchone()
    if row is None:
        print("Item not found")
    else:
        print(row)
    return

# 5.7
def searchonitemname():
    global cursor
    global conn
    itemname = input("Enter item name: ")
    cursor.execute("SELECT * FROM istock WHERE itemname = %s", (itemname,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return

# 5.8
def searchissue_purchaselist():
    global cursor
    global conn
    transactiontype = input("Enter transaction type: ")
    if transactiontype == "P":
        cursor.execute("SELECT * FROM istock WHERE quantity > 0")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif transactiontype == "I":
        cursor.execute("SELECT * FROM istock WHERE quantity < 0")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("Invalid transaction type")
    return