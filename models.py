from database import get_connection
from datetime import datetime

def update_salary(new_salary):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT salary, savings FROM user WHERE id=1")
    old_salary, savings = cur.fetchone()

    if new_salary < old_salary:
        conn.close()
        return False, "Salary cannot be reduced"

    increment = new_salary - old_salary
    savings += increment * 0.15

    cur.execute(
        "UPDATE user SET salary=?, savings=? WHERE id=1",
        (new_salary, savings)
    )

    conn.commit()
    conn.close()
    return True, increment * 0.15

def add_expense(category, amount):
    if amount <= 0:
        return False

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)",
        (category, amount, datetime.now().strftime("%Y-%m-%d"))
    )

    conn.commit()
    conn.close()
    return True

def get_category_expenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    data = cur.fetchall()
    conn.close()
    return data

def get_summary():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT salary, savings FROM user WHERE id=1")
    salary, savings = cur.fetchone()

    cur.execute("SELECT SUM(amount) FROM expenses")
    expenses = cur.fetchone()[0] or 0

    conn.close()
    return salary, savings, expenses
