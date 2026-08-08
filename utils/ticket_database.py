import sqlite3
import os

DATABASE = "database/users.db"


def initialize_ticket_database():

    os.makedirs("database", exist_ok=True)

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            ticket_id TEXT UNIQUE,

            username TEXT NOT NULL,

            title TEXT NOT NULL,

            category TEXT NOT NULL,

            priority TEXT NOT NULL,

            description TEXT NOT NULL,

            status TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()