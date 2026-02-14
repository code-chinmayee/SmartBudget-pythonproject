import sqlite3

def get_connection():
    return sqlite3.connect("budget.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        salary REAL,
        savings REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    """)

    cursor.execute("SELECT * FROM user")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO user VALUES (1, 0, 0)")

    conn.commit()
    conn.close()
