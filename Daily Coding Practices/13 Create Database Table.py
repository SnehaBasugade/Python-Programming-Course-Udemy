import sqlite3

conn=sqlite3.connect("Company.db")
print("Database connected successfully")

cursor=conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS
               employees(id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age Integer,
               departement TEXT
               )
               ''')
conn.commit()
conn.close()
print("Table created successfully and connect")