import sqlite3

DATABASE_NAME = "passwords.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT UNIQUE
        )
    """)

    conn.commit()
    conn.close()


def password_exists(password_hash):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM passwords WHERE password_hash = ?",
        (password_hash,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_password(password_hash):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO passwords(password_hash) VALUES(?)",
        (password_hash,)
    )

    conn.commit()
    conn.close()