import sqlite3


conn=sqlite3.connect("company.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM employees")
rows=conn.cursor()

for row in rows:
    print(row[0])
    
    conn.close()