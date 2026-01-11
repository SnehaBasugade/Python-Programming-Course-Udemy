import sqlite3

conn=sqlite3.connect("company.db")
cursor=conn.cursor()

emp_id=int(input("Enter employee ID to update"))