import sqlite3
import os

DATABASE = "database/users.db"

print("LOGIN DATABASE PATH:")
print(os.path.abspath(DATABASE))


def login_user(username, password):

    print("Entered Username:", repr(username))
    print("Entered Password:", repr(password))

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT username,password,role,full_name,status
        FROM users
    """)

    print("\nDATABASE CONTENTS:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("""
        SELECT username,role,full_name
        FROM users
        WHERE username=?
        AND password=?
        AND status='Active'
    """,(username,password))

    user = cursor.fetchone()

    print("\nMATCH FOUND:", user)

    connection.close()

    return user