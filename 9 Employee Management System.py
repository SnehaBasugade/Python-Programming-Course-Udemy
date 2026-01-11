import sqlite3


def get_connection():
    conn = sqlite3.connect("employee_management.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables():
    conn, cursor = get_connection()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id INTEGER,
            project_name TEXT,
            FOREIGN KEY (emp_id) REFERENCES employees(id)
        )
    """)

    conn.commit()
    conn.close()


def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")

    conn, cursor = get_connection()
    cursor.execute(
        "INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
        (name, age, department)
    )
    conn.commit()
    conn.close()
    print("Employee added successfully!\n")

def view_employees():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
    print()

def search_by_department():
    dept = input("Enter department to search: ")

    conn, cursor = get_connection()
    cursor.execute(
        "SELECT * FROM employees WHERE department = ?",
        (dept,)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
    print()

def update_employee():
    emp_id = input("Enter employee ID to update: ")
    new_dept = input("Enter new department: ")

    conn, cursor = get_connection()
    cursor.execute(
        "UPDATE employees SET department = ? WHERE id = ?",
        (new_dept, emp_id)
    )

    conn.commit()
    conn.close()
    print("Employee updated successfully!\n")

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")

    conn, cursor = get_connection()
    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )

    conn.commit()
    conn.close()
    print("Employee deleted successfully!\n")

def assign_project():
    emp_id = input("Enter employee ID: ")
    project = input("Enter project name: ")

    conn, cursor = get_connection()
    cursor.execute(
        "INSERT INTO projects (emp_id, project_name) VALUES (?, ?)",
        (emp_id, project)
    )

    conn.commit()
    conn.close()
    print("Project assigned successfully!\n")

def view_employees_with_projects():
    conn, cursor = get_connection()
    cursor.execute("""
        SELECT employees.name, employees.department, projects.project_name
        FROM employees
        INNER JOIN projects ON employees.id = projects.emp_id
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
    print()


def menu():
    create_tables()

    while True:
        print("=== Employee Management System ===")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employees by Department")
        print("4. Update Employee Department")
        print("5. Delete Employee")
        print("6. Assign Project to Employee")
        print("7. View Employees with Projects")
        print("8. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_by_department()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            assign_project()
        elif choice == '7':
            view_employees_with_projects()
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()
