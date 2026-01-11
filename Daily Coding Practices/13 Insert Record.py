import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO employees (name, age, department) 
    VALUES (?, ?, ?) 
''', ("Ali", 31, "Human Resource"))

conn.commit()
conn.close()
print("Inserted Successfully!")
