import sqlite3

DATABASE = "database/users.db"


# ==========================================
# Generate Ticket ID
# ==========================================

def generate_ticket_id():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ticket_id
        FROM tickets
        ORDER BY id DESC
        LIMIT 1
    """)

    last_ticket = cursor.fetchone()

    connection.close()

    if last_ticket is None:
        return "TKT-1001"

    last_number = int(last_ticket[0].split("-")[1])

    return f"TKT-{last_number + 1}"


# ==========================================
# Create Ticket
# ==========================================

def create_ticket(
    username,
    title,
    category,
    priority,
    description
):

    ticket_id = generate_ticket_id()

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tickets(

            ticket_id,
            username,
            title,
            category,
            priority,
            description,
            status

        )

        VALUES(?,?,?,?,?,?,?)
        """,
        (
            ticket_id,
            username,
            title,
            category,
            priority,
            description,
            "Open"
        )
    )

    connection.commit()
    connection.close()

    return ticket_id


# ==========================================
# Get User Tickets
# ==========================================

def get_user_tickets(username):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            ticket_id,
            title,
            category,
            priority,
            status,
            created_at
        FROM tickets
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    tickets = cursor.fetchall()

    connection.close()

    return tickets


# ==========================================
# Get Ticket Details
# ==========================================

def get_ticket_details(ticket_id):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            ticket_id,
            username,
            title,
            category,
            priority,
            description,
            status,
            created_at
        FROM tickets
        WHERE ticket_id=?
        """,
        (ticket_id,)
    )

    ticket = cursor.fetchone()

    connection.close()

    return ticket


# ==========================================
# Update Ticket
# ==========================================

def update_ticket(
    ticket_id,
    title,
    category,
    priority,
    description
):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tickets

        SET
            title=?,
            category=?,
            priority=?,
            description=?

        WHERE ticket_id=?
        """,
        (
            title,
            category,
            priority,
            description,
            ticket_id
        )
    )

    connection.commit()

    connection.close()

# ==========================================
# Cancel Ticket
# ==========================================

def cancel_ticket(ticket_id):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tickets

        SET status=?

        WHERE ticket_id=?
        """,
        (
            "Cancelled",
            ticket_id
        )
    )

    connection.commit()

    connection.close()