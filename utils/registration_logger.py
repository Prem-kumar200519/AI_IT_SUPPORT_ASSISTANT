import os
from datetime import datetime

def log_registered_user(full_name, email, username, password, role, status):

    print("Current Working Directory:", os.getcwd())

    os.makedirs("logs", exist_ok=True)

    file_path = "logs/registered_users.txt"

    print("Saving to:", os.path.abspath(file_path))

    with open(file_path, "a", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write(f"Date      : {datetime.now()}\n")
        file.write(f"Full Name : {full_name}\n")
        file.write(f"Email     : {email}\n")
        file.write(f"Username  : {username}\n")
        file.write(f"Password  : {password}\n")
        file.write(f"Role      : {role}\n")
        file.write(f"Status    : {status}\n")
        file.write("=" * 50 + "\n\n")

    print("User log saved successfully!")