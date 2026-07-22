import json
import os
import random
from datetime import datetime


TICKET_FILE = "data/tickets.json"


def load_tickets():

    if not os.path.exists(TICKET_FILE):

        with open(TICKET_FILE, "w") as f:
            json.dump([], f)

    with open(TICKET_FILE, "r") as f:
        return json.load(f)


def save_tickets(tickets):

    with open(TICKET_FILE, "w") as f:
        json.dump(tickets, f, indent=4)


def generate_ticket_id():

    date = datetime.now().strftime("%Y%m%d")

    number = random.randint(1000, 9999)

    return f"INC-{date}-{number}"


def get_priority(issue):

    issue = issue.lower()

    high = [
        "server",
        "database",
        "crash",
        "critical",
        "down",
        "security"
    ]

    medium = [
        "vpn",
        "wifi",
        "network",
        "login",
        "password",
        "printer"
    ]

    for word in high:

        if word in issue:
            return "High"

    for word in medium:

        if word in issue:
            return "Medium"

    return "Low"


def create_ticket(issue):

    ticket = {

        "Ticket ID": generate_ticket_id(),

        "Issue": issue,

        "Priority": get_priority(issue),

        "Status": "Open",

        "Assigned Team": "IT Support",

        "Created": datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )
    }

    tickets = load_tickets()

    tickets.append(ticket)

    save_tickets(tickets)

    return ticket