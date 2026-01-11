import sqlite3

conn=sqlite3.connect("company.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM employees WHERE age>25")
rows=cursor.fetchall()

for row in rows:
    print(row)