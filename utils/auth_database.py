import sqlite3
DATABASE_PATH = "database/users.db"
import os

print("AUTH DATABASE PATH:")
print(os.path.abspath(DATABASE_PATH))


def initialize_database():

    # Create database folder if it doesn't exist
    os.makedirs("database", exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT NOT NULL,

            email TEXT NOT NULL UNIQUE,

            username TEXT NOT NULL UNIQUE,

            password TEXT NOT NULL,

            role TEXT NOT NULL,

            status TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # Check whether admin already exists
    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        ("admin",)
    )

    admin = cursor.fetchone()

    if admin is None:

        cursor.execute("""
            INSERT INTO users(
                full_name,
                email,
                username,
                password,
                role,
                status
            )

            VALUES(
                ?,?,?,?,?,?
            )
        """, (

            "prem kumar",
            "premkumarsrinivasan200519@gmail.com",
            "admin",
            "Prem_19...@",
            "Admin",
            "Active"

        ))

    connection.commit()

    connection.close()